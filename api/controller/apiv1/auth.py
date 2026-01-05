#!/usr/bin/env python
from flask import request
from flask_jwt_extended import create_access_token
from api.model import User
from api.util import jsonify


class AuthController:
    @classmethod
    def login(cls):
        try:
            data = request.get_json()
            current_user = User.find_by_username(data['username'])
            if not current_user:
                return jsonify(status=404, code=401)
            if User.verify_hash(data['password'], current_user.password):
                access_token = create_access_token(identity=data['username'])
                return jsonify({"result": {"message": "Logged in as {}".format(current_user.username),
                                           "access_token": access_token}}, status=200)
            else:
                return jsonify(status=401, code=401)
        except Exception as e:
            return jsonify(status=500, code=102)
