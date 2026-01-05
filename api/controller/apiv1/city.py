#!/usr/bin/env python
from flask import request
from api.model import City, Country
from api.schema.apiv1.city import CitySchema
from api.util import jsonify
# from sqlalchemy import or_ as OR
from api.api import db
from api.util.pagination import paginate


class CityController:
    @staticmethod
    def get_cities():
        city_schema = CitySchema(many=True)
        try:
            cities = City.query
            return paginate(cities, city_schema)
        except:
            return jsonify(status=500, code=102)

    @staticmethod
    def get_city(city_id):
        city_schema = CitySchema()
        try:
            city = City.query.get(city_id)
        except:
            return jsonify(status=500, code=102)
        if city is None:
            return jsonify(status=404, code=103)
        return jsonify({"city": city_schema.dump(city)})

    @staticmethod
    def create_city():
        city_schema = CitySchema()
        data = request.get_json()
        if not data or "name" not in data or "country_code" not in data:
            return jsonify(status=400, code=101)
        try:
            # Check if country exists
            country = Country.query.filter_by(code=data["country_code"].upper()).first()
            if not country:
                return jsonify(status=404, code=107)  # Country not found

            city = City(
                name=data["name"].lower(),
                country_code=data["country_code"].upper(),
                population=data.get("population"),
                country_id=country.id
            )
            db.session.add(city)
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify(
            {"city": city_schema.dump(city)},
            status=201
        )

    @staticmethod
    def update_city(city_id):
        city_schema = CitySchema()
        errors = city_schema.validate(request.json)
        if errors:
            return jsonify(status=400, code=104)  # Request validation failed.
        data = request.get_json()
        if not data:
            return jsonify(status=400, code=101)
        try:
            city = City.query.get(city_id)
        except:
            return jsonify(status=500, code=102)
        if city is None:
            return jsonify(status=404, code=103)

        if "name" in data:
            city.name = data["name"].lower()

        if "country_code" in data:
            # Verify new country exists
            country = Country.query.filter_by(code=data["country_code"].upper()).first()
            if not country:
                return jsonify(status=404, code=107)  # Country not found
            city.country_code = data["country_code"].upper()
            city.country_id = country.id

        if "population" in data:
            city.population = data["population"]

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify(
            {"city": city_schema.dump(city)}
        )

    @staticmethod
    def delete_city(city_id):
        city = City.query.get(city_id)
        if city is None:
            return jsonify(status=404, code=103)

        try:
            db.session.delete(city)
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify(status=204)
