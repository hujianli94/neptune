from sqlalchemy import or_ as OR
from api.api import db
from api.model import Country
from api.schema.apiv1 import CountrySchema
from api.util import jsonify
from api.util.pagination import paginate
from flask_jwt_extended import jwt_required


class CountryController(object):
    @classmethod
    def get_countries(cls):
        countries_schema = CountrySchema(many=True)
        try:
            countries = Country.query
            return paginate(countries, countries_schema)
        except:
            return jsonify(status=500, code=102)

    @classmethod
    def get_country(cls, country_id):
        country_schema = CountrySchema()
        try:
            country = Country.query.get(country_id)
        except:
            return jsonify(status=500, code=102)  # Database error.
        if country is None:
            return jsonify(status=404, code=103)  # Country is not found.
        return jsonify(
            {"country": country_schema.dump(country)}
        )

    @staticmethod
    @jwt_required()
    def create_country(country_data):
        country_schema = CountrySchema()
        errors = country_schema.validate(country_data)
        if errors:
            return jsonify(status=400, code=104)  # Request validation failed.
        try:
            data = country_schema.load(country_data)
        except:
            return jsonify(status=400, code=104)  # Request validation failed.
        if not data["code"] or not data["name"] or not data["capital"]:
            return jsonify(status=400, code=105)  # Empty data.
        try:
            country = Country.query.filter(
                OR(
                    Country.code == data["code"].upper(),
                    Country.name == data["name"].lower()
                )
            ).first()  # Select country to find any conflicts.
        except:
            return jsonify(status=500, code=102)  # Database error.
        if country is not None:
            return jsonify(status=409, code=106)
        country = Country(
            code=data["code"].upper(),
            name=data["name"].lower(),
            capital=data["capital"].lower(),
            longitude=data["longitude"] if "longitude" in data else 1,
            latitude=data["latitude"] if "latitude" in data else 1,
        )
        db.session.add(country)
        try:
            db.session.commit()  # Database INSERT query.
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)  # Database error.
        return jsonify(
            {"country": country_schema.dump(country)},
            status=201
        )

    @staticmethod
    @jwt_required()
    def update_country(country_id, data, partial=False):  # Add partial parameter
        country_schema = CountrySchema()
        errors = country_schema.validate(data)
        if errors:
            return jsonify(status=400, code=104)  # Request validation failed.
        try:
            data = country_schema.load(data, partial=partial)
        except:
            return jsonify(status=400, code=104)  # Request validation failed.
        try:
            country = Country.query.get(country_id)
        except:
            return jsonify(status=500, code=102)  # Database error.
        if country is None:
            return jsonify(status=404, code=103)  # Country is not found.
        if "code" in data:
            country.code = data["code"].upper()
        if "name" in data:
            country.name = data["name"].lower()
        if "capital" in data:
            country.capital = data["capital"].lower()
        if "longitude" in data:
            country.longitude = data["longitude"]
        if "latitude" in data:
            country.latitude = data["latitude"]
        try:
            db.session.commit()  # Database UPDATE query.
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)  # Database error.
        return jsonify(
            {"country": country_schema.dump(country)}
        )

    @staticmethod
    @jwt_required()
    def delete_country(country_id):
        try:
            country = Country.query.get(country_id)
        except:
            return jsonify(status=500, code=102)  # Database error.
        if country is None:
            return jsonify(status=404, code=103)  # Country is not found.
        try:
            db.session.delete(country)  # Database DELETE query.
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)  # Database error.
        return jsonify(status=204)
