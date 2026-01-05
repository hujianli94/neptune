from api.api import ma
from api.model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        load_instance = True  # This will make load() return User instances

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(required=True)
    password = ma.auto_field(required=True)
