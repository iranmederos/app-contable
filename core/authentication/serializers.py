from .models import CustomUser, Role
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model= CustomUser
        fields= '__all__'


class RoleSerializer(ModelSerializer):

    class Meta:
        model= Role
        fields= '__all__'