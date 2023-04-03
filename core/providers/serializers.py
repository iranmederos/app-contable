from .models import Provider
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class ProviderSerializer(ModelSerializer):

    class Meta:
        model= Provider
        fields= '__all__'
