from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets

# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    serializer_class= CustomerSerializer
    queryset= Customer.objects.all()