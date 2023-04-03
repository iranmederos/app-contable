from django.db import models




TYPE_NAC=(('1','Nacional'),('2','Extranjero'))
TYPE_PERSON=(('1',''),('2',''))
TYPE_TAXPAYER=(('1',''),('2',''))

class RegistrationData(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    constitution_date= models.DateField(null=False, blank=False)
    registration_date= models.DateField(null=False, blank=False)
    registration_number= models.CharField(null=False, blank=False, unique=True, max_length=50)
    registration_office= models.CharField(null=False, blank=False, max_length=50)
    registration_city= models.CharField(null=False, blank=False,  max_length=50)



class Company(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
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
    domiciled= models.BooleanField(null=False, blank=False, unique=True)
    nacionality= models.CharField(choices=TYPE_NAC, null=False, blank=False, unique=True)
    #Averiguar tipo exacto!
    exempt_income= models
    economic_denomination= models.CharField(null=False, blank=False)
    #crear las tuplas correspondientes
    type_person= models.CharField(choices=TYPE_PERSON, null=False, blank=False)
    type_taxpayer= models.CharField(choices=TYPE_TAXPAYER, null=False, blank=False)
    registration_data= models.OneToOneField(RegistrationData, null=False, blank=False, unique=True)


