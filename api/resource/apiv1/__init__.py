from api.api import apiv1 as api
from api.resource.apiv1.country import CountryResource
from api.resource.apiv1.city import CityResource, CityIdResource
from api.resource.apiv1.users import UsersResource
from api.resource.apiv1.auth import AuthResource

api.add_resource(
    CountryResource,
    "/countries",
    methods=["GET", "POST"],
    endpoint="countries"
)
api.add_resource(
    CountryResource,
    "/countries/<country_id>",
    methods=["GET", "PATCH", "PUT", "DELETE"],
    endpoint="country"
)
api.add_resource(
    CityResource,
    "/cities",
    methods=["GET", "POST"],
    endpoint="cities"
)
api.add_resource(
    CityIdResource,
    "/cities/<city_id>",
    methods=["GET", "PUT", "DELETE"],
    endpoint="city"
)

api.add_resource(
    UsersResource,
    "/users",
    methods=["POST"],
    endpoint="users"
)

api.add_resource(
    AuthResource,
    "/login",
    methods=["POST"],
    endpoint="login"
)
