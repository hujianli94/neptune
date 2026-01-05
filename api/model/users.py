#!/usr/bin/env python
from api.api import db
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # unique id for each user
    username = db.Column(db.String(120), unique=True, nullable=False)  # username for login
    password = db.Column(db.String(120), nullable=False)  # hashed password for login

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
