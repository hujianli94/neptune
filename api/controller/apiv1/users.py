#!/usr/bin/env python
from flask import request
from flask_jwt_extended import create_access_token
from api.model import User
from api.schema.apiv1.users import UserSchema
from api.util import jsonify
from api.api import db


class UsersController:
    @classmethod
    def create_user(cls):
        try:
            data = request.get_json()
            if 'password' not in data:
                return jsonify(status=400, code=105)  # Empty data

            # Check if username already exists
            if User.find_by_username(data.get('username')):
                return jsonify(status=409, code=106)  # Conflict - username exists

            data['password'] = User.generate_hash(data['password'])
            user_schema = UserSchema()

            # Create user instance and add to session
            user = user_schema.load(data)
            db.session.add(user)
            db.session.commit()

            return jsonify({"result": user_schema.dump(user)}, status=201)

        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {str(e)}")
            if "password" in str(e).lower():
                return jsonify(status=400, code=104)
            return jsonify(status=500, code=102)
