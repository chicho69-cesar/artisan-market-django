from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'is_admin', 'email', 'name', 'lastname', 'picture', 'biography']
        # TODO: Poner el role_id cuando añada las relaciones

    def get_is_admin(self, obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'is_admin', 'email', 'name', 'lastname', 'picture', 'biography', 'token']
        # TODO: Poner el role_id cuando añada las relaciones

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
