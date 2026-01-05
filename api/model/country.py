from api.api import db
from api.util import uuidgen


class Country(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=uuidgen)  # UUID
    code = db.Column(db.String(10), unique=True, index=True, nullable=False)  # 国家代码 (如 IRN)
    name = db.Column(db.String(100), unique=True, index=True, nullable=False)  # 国家名称
    capital = db.Column(db.String(64), index=True, nullable=False)  # 首都
    longitude = db.Column(db.Float, nullable=False, default=1)  # 经度
    latitude = db.Column(db.Float, nullable=False, default=1)  # 纬度
    cities = db.relationship('City', backref='country', lazy='dynamic', cascade='all, delete-orphan')  # 关联城市
