from flask import request
from flask_restful import Resource
from api.controller.apiv1 import CountryController
from api.util import jsonify


class CountryResource(Resource):
    def get(self, country_id=None):
        """
        GET /countries --> List of countries.
        GET /countries/<country_id> --> Country info.
        """
        if country_id is None:
            return CountryController.get_countries()  # List of countries.
        return CountryController.get_country(country_id)  # Country info.

    def post(self):
        """
        POST /countries --> Create new country.
        """
        return CountryController.create_country(request.get_json())  # Create new country.

    def patch(self, country_id):
        """
        PATCH /countries/<country_id> --> Update country location (longitude/latitude).
        """
        data = request.get_json()
        # Only allow longitude and latitude updates
        allowed_fields = ['longitude', 'latitude']
        filtered_data = {k: v for k, v in data.items() if k in allowed_fields}
        if not filtered_data:
            return jsonify(status=400, code=104)  # No valid fields to update
        return CountryController.update_country(country_id, filtered_data, partial=True)

    def put(self, country_id):
        """
        PUT /countries/<country_id> --> Update country info.
        """
        return CountryController.update_country(country_id, request.get_json())  # Update country info.

    def delete(self, country_id):
        """
        DELETE /countries/<country_id> --> Delete country.
        """
        return CountryController.delete_country(country_id)  # Delete country.
