from django.db import models
from company.models import Company


TYPE_SALES=(('1',''),('2',''))
TYPE_TAXPAYER=(('1',''),('2',''))
TYPE_PERSON=(('1',''),('2',''))

class Provider(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    rif= models.CharField(null=False, blank=False, max_length=20)
    business_name= models.CharField(null=False, blank=False, max_length=20)
    domiciled= models.BooleanField(null=False, blank=False)
    address= models.CharField(null=False, blank=False, max_length=100)
    number_phone= models.CharField(null=False, blank=False, max_length=20)
    tax_residence= models.CharField(null=False, blank=False, max_length=100)
    ret_iva= models.BooleanField(null=False, blank=False)
    percent_iva= models.FloatField(null=False, blank=False)
    type_person= models.CharField(choices=TYPE_PERSON, null=False, blank=False)
    type_taxpayer= models.CharField(choices=TYPE_TAXPAYER, null=False, blank=False)
    type_sales= models.CharField(TYPE_SALES,null=False, blank=False)
    company= models.ForeignKey(Company, null=False, blank=False) 
