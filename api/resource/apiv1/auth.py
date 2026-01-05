#!/usr/bin/env python
from flask_restful import Resource
from api.controller.apiv1 import AuthController


class AuthResource(Resource):
    def post(self):
        return AuthController.login()
