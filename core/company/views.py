from django.shortcuts import render
from .serializers import CompanySerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Company
# Create your views here.



class CompanyCreate(CreateAPIView):
    serializer_class = CompanySerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message":"Empresa creada exitosamente", "Numero de rif": serializer.data['rif']},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al registrar paciente: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

class UpdatePatient(UpdateAPIView):
    serializer_class = CompanySerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def update(self, request, rif_arg):
        patient = get_object_or_404(Company, rif=rif_arg)
        serializer = self.get_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Emperesa actualizada exitosamente"})