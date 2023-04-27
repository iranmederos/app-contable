from .serializers import PurchaseDocument, DocumentTypeSerializer, ItemDocumentSerializer, PurchaseDocumentSerializer, SaleDocumentSerializer, SaleSummarySerializer, RentIVASerializer
from .models import DocumentType, ItemDocument, PurchaseDocument, SaleSummary, SaleDocument, RetIVA
from rest_framework import viewsets
# Create your views here.


class PurchaseDocumentView(viewsets.ModelViewSet):
    serializer_class = PurchaseDocumentSerializer
    queryset = PurchaseDocument.objects.all()


class DocumentTypeView(viewsets.ModelViewSet):
    serializer_class = DocumentTypeSerializer
    queryset = DocumentType.objects.all()


class ItemDocumentView(viewsets.ModelViewSet):
    serializer_class = ItemDocumentSerializer
    queryset = ItemDocument.objects.all()


class SaleSummaryView(viewsets.ModelViewSet):
    serializer_class = SaleSummarySerializer
    queryset = SaleSummary.objects.all()


class SaleDocumentView(viewsets.ModelViewSet):
    serializer_class = SaleDocumentSerializer
    queryset = SaleDocument.objects.all()


class RetIVAView(viewsets.ModelViewSet):
    serializer_class = RentIVASerializer
    queryset = RetIVA.objects.all()
