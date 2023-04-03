from .models import SalesDocument,SalesSummary,BuysDocument,Totals,DocumentsItems,DocumentType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class SalesDocumentSerializer(ModelSerializer):

    class Meta:
        model= SalesDocument
        fields= '__all__'


class SalesSummarySerializer(ModelSerializer):

    class Meta:
        model= SalesSummary
        fields= '__all__'

class BuysDocumentSerializer(ModelSerializer):

    class Meta:
        model= BuysDocument
        fields= '__all__'

class TotalsSerializer(ModelSerializer):

    class Meta:
        model= Totals
        fields= '__all__'

class DocumentsItemsSerializer(ModelSerializer):

    class Meta:
        model= DocumentsItems
        fields= '__all__'

class DocumentTypeSerializer(ModelSerializer):

    class Meta:
        model= DocumentType
        fields= '__all__'