from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

class GetUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']