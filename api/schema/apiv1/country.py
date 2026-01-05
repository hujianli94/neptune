from api.api import ma
from api.model import Country
from api.schema.apiv1.city import CitySchema


class CountrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Country

    id = ma.auto_field(dump_only=True)
    code = ma.auto_field(required=False)
    name = ma.auto_field(required=False)
    capital = ma.auto_field(required=False)
    longitude = ma.auto_field(required=False)
    latitude = ma.auto_field(required=False)
    cities = ma.Nested(CitySchema, many=True, dump_only=True)
