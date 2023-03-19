from rest_framework import serializers
from djoser.serializers import UserSerializer
from . import models

class BaseUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model=models.BaseUser
        fields=['id','username','email','first_name','last_name']


class BaseUserCreateSerializer(UserSerializer):
    username=serializers.CharField()

    class Meta(UserSerializer.Meta):
        model=models.BaseUser
        fields=['id','username','email','first_name','last_name','password']