from .serializers import TaxMachineSerializer
from .models import TaxMachine
from rest_framework import viewsets

# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    serializer_class= TaxMachineSerializer
    queryset= TaxMachine.objects.all()