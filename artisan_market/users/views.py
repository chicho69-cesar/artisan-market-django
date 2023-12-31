from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user_serializers = UserSerializerWithToken(self.user).data

        for token, user in user_serializers.items():
            data[token] = user

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def sign_up(request):
    data = request.data

    try:
        # TODO: Hacer lo del role_id cuando añada las relaciones
        user = User.objects.create(
            email=data['email'],
            password=make_password(data['password']),
            name=data['name'],
            lastname=data['lastname'],
            picture=data['picture'],
            biography=data['biography']
            # role_id=created_role_id
        )

        serializer = UserSerializerWithToken(user, many=False)

        return Response(serializer.data)
    except:
        message = {'detail': 'Error registering the user!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
