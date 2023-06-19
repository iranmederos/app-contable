from django.db import models


class RegistrationData(models.Model):
    constitution_date= models.DateField(null=False, blank=False)
    registration_date= models.DateField(null=False, blank=False)
    registration_number= models.CharField(null=False, blank=False, unique=True, max_length=50)
    registration_office= models.CharField(null=False, blank=False, max_length=50)
    registration_city= models.CharField(null=False, blank=False,  max_length=50)

    class Meta:
        verbose_name = ("Registration date")
        verbose_name_plural = ("Registration date")

    def __str__(self) -> str:
        return self.registration_number

class Company(models.Model):
    TYPE_NAC=(('1','Nacional'),('2','Extranjero'))
    TYPE_PERSON=(('1','Natural'),('2','Juridica'))
    TYPE_TAXPAYER=(('1','Formal'),('2','Ordinario'),('3','Especial'),('4','Publico'),('5','No Especial'))

    name= models.CharField(null=False, blank=False, unique=True, max_length=50)
    business_name= models.CharField(null=False, blank=False, unique=True, max_length=50)
    fiscal_period_ini= models.DateField(null=False, blank=False)
    fiscal_period_end= models.DateField(null=False, blank=False)
    rif= models.CharField(null=False, blank=False, unique=True, max_length=20)
    rif_second= models.CharField(null=False, blank=False, unique=True, max_length=20)
    ret_iva= models.FloatField(null=False, blank=True)
    tax_residence= models.CharField(null=False, blank=False, max_length=100)
    number_phone= models.CharField(null=False, blank=False, unique=True, max_length=20)
    email= models.CharField(null=False, blank=False, unique=True, max_length=20)
    domiciled= models.BooleanField(null=False, blank=False)
    nacionality= models.CharField(choices=TYPE_NAC, null=False, blank=False, max_length=20)
    exempt_income= models.BooleanField(null=False, blank=False)
    economic_denomination= models.CharField(null=False, blank=False, max_length=20)
    type_person= models.CharField(choices=TYPE_PERSON, null=False, blank=False, max_length=20)
    type_taxpayer= models.CharField(choices=TYPE_TAXPAYER, null=False, blank=False, max_length=20)
    registration_data= models.OneToOneField(RegistrationData, on_delete=models.CASCADE, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    def __str__(self) -> str:
        return self.business_name
