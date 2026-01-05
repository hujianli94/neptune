#!/usr/bin/env python

from api.api import ma
from api.model import City


class CitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = City
        fields = ('id', 'name', 'country_code', 'population')

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=False)  # Make optional
    country_code = ma.auto_field(required=False)  # Make optional
    population = ma.auto_field(required=False)  # Make optional
