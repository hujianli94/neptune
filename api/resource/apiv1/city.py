#!/usr/bin/env python
from flask_restful import Resource
from api.controller.apiv1 import CityController


class CityResource(Resource):
    def get(self):
        return CityController.get_cities()

    def post(self):
        return CityController.create_city()


class CityIdResource(Resource):
    def get(self, city_id):
        return CityController.get_city(city_id)

    def put(self, city_id):
        return CityController.update_city(city_id)

    def delete(self, city_id):
        return CityController.delete_city(city_id)
