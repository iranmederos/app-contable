from .models import SaleDocument,SaleSummary,PurchaseDocument,ItemDocument,DocumentType,RetIVA
from rest_framework.serializers import ModelSerializer


class SaleDocumentSerializer(ModelSerializer):

    class Meta:
        model= SaleDocument
        fields= '__all__'


class SaleSummarySerializer(ModelSerializer):

    class Meta:
        model= SaleSummary
        fields= '__all__'

class PurchaseDocumentSerializer(ModelSerializer):

    class Meta:
        model= PurchaseDocument
        fields= '__all__'


class ItemDocumentSerializer(ModelSerializer):

    class Meta:
        model= ItemDocument
        fields= '__all__'

class DocumentTypeSerializer(ModelSerializer):

    class Meta:
        model= DocumentType
        fields= '__all__'

class RentIVASerializer(ModelSerializer):

    class Meta:
        model= RetIVA
        fields= '__all__'