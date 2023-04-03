from .models import Company, RegistrationData
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CompanySerializer(ModelSerializer):

    class Meta:
        model= Company
        fields= '__all__'


class RegistrationDataSerializer(ModelSerializer):

    class Meta:
        model= RegistrationData
        fields= '__all__'