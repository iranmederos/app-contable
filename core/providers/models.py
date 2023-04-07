from django.db import models
from company.models import Company


TYPE_SALES=(('1','Interna'),('2','Exportacion'))
TYPE_TAXPAYER=(('1','Contribuyente'),('2','No contribuyente'))
TYPE_PERSON=(('1','Natural'),('2','Juridico'))

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
    type_person= models.CharField(choices=TYPE_PERSON, null=False, blank=False, max_length=20)
    type_taxpayer= models.CharField(choices=TYPE_TAXPAYER, null=False, blank=False, max_length=20)
    type_sales= models.CharField(choices=TYPE_SALES,null=False, blank=False, max_length=20)
    ret_code= models.CharField(null=False, blank=False, max_length=15, default=None)
    company= models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=False, blank=False, default=None) 

    def __str__(self) -> str:
        return self.business_name