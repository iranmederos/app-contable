from .serializers import CompanySerializer, RegistrationDataSerializer
from rest_framework import viewsets
#from rest_framework.response import Response
#from rest_framework import status
#from django.shortcuts import get_object_or_404
from .models import Company, RegistrationData
# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class RegistrationDataView(viewsets.ModelViewSet):
    serializer_class = RegistrationDataSerializer
    queryset = RegistrationData.objects.all()
    

   