from .serializers import ProviderSerializer
from .models import Provider
from rest_framework import viewsets

# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    serializer_class= ProviderSerializer
    queryset= Provider.objects.all()