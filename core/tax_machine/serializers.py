from .models import TaxMachine
from rest_framework.serializers import ModelSerializer


class TaxMachineSerializer(ModelSerializer):

    class Meta:
        model= TaxMachine
        fields= '__all__'
