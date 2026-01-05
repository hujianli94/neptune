#!/usr/bin/env python
from flask_restful import Resource
from api.controller.apiv1 import UsersController


class UsersResource(Resource):
    def post(self):
        # For user registration
        return UsersController().create_user()
