#!/usr/bin/env python
from api.api import db


# from api.util import uuidgen


class City(db.Model):
    # id = db.Column(db.String(32), primary_key=True, default=uuidgen)  # UUID
    id = db.Column(db.Integer, primary_key=True)  # 自增id
    name = db.Column(db.String(100))  # 城市名称
    country_code = db.Column(db.String(10), nullable=False)  # 国家代码
    population = db.Column(db.Integer)  # 人口
    country_id = db.Column(db.String(32), db.ForeignKey('country.id'), nullable=False)  # 关联国家
