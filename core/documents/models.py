from django.db import models
from customers import models as cust
from providers import models as pr

TYPE_RECORD= (("1","Registro"),("2","Complemeto"),("3","Anulación"),("4","Ajuste"))
TYPE_MACHINE=(("1","Registradora con mem. fiscal"),("2","Impresora fiscal"),("3","Computadora con mem. fiscal"))

class DocumentType(models.Model):
    type_doc= models.CharField(null=False, blank=False, max_length=15)

    def __str__(self) -> str:
        return self.type_doc

class Totals(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    amount= models.FloatField(null=False, blank=False)
    gross_amount= models.FloatField(null=False, blank=False)
    iva_amount= models.FloatField(null=False, blank=False)
    neto_amount= models.FloatField(null=False, blank=False)


class SalesDocument(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    branch= models.CharField(null=False, blank=False, max_length=20)
    document_number= models.CharField(null=False, blank=False, max_length=20)
    ctrl_number= models.CharField(null=False, blank=False, max_length=20)
    issuance_date= models.DateField(null=False, blank=False)
    registration_date= models.DateField(null=False, blank=False)
    state= models.CharField(null=False, blank=False, max_length=20)
    type_record= models.CharField(choices=TYPE_RECORD,null=False, blank=False, max_length=20)
    document_type= models.ForeignKey(DocumentType,on_delete=models.DO_NOTHING, null=False, blank=False)
    customer_code= models.ForeignKey(cust.Customer, on_delete=models.DO_NOTHING, default=None)
    
    

class BuysDocument(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    branch= models.CharField(null=False, blank=False, max_length=20)
    document_number= models.CharField(null=False, blank=False, max_length=20)
    ctrl_number= models.CharField(null=False, blank=False, max_length=20)
    issuance_date= models.DateField(null=False, blank=False, max_length=20)
    registration_date= models.DateField(null=False, blank=False)
    state= models.CharField(null=False, blank=False, max_length=20)
    type_record= models.CharField(choices=TYPE_RECORD,null=False, blank=False, max_length=20)
    document_type= models.ForeignKey(DocumentType,on_delete=models.DO_NOTHING, null=False, blank=False)
    provider_code= models.ForeignKey(pr.Provider, on_delete=models.DO_NOTHING, default=None)
   

class SalesSummary(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    code= models.CharField(null=False, blank=False, max_length=20)
    description= models.CharField(null=False, blank=False, max_length=50)
    type= models.CharField(choices=TYPE_MACHINE, null=False, blank=False, max_length=20)
    serial= models.CharField(null=False, blank=False, max_length=20)
    model= models.CharField(null=False, blank=False, max_length=20)
    n_invoice= models.CharField(null=False, blank=False, max_length=20)
    zeta= models.CharField(null=False, blank=False, max_length=20)
    since= models.DateTimeField(null=False, blank=False) 
    until= models.DateTimeField(null=False, blank=False) 


class DocumentsItems(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    description= models.CharField(null=False, blank=False, max_length=100)
    amount= models.FloatField(null=False, blank=False)
    iva= models.FloatField(null=False, blank=False)
    amount_iva= models.FloatField(null=False, blank=False)
    c_ctrl= models.FloatField(null=False, blank=False)
    patente= models.FloatField(null=False, blank=False)
    ret= models.FloatField(null=False, blank=False)
    sale_document= models.OneToOneField(SalesDocument, on_delete=models.DO_NOTHING, default=None,null=True, blank=True)
    buy_document= models.OneToOneField(BuysDocument, on_delete=models.DO_NOTHING, default=None,null=True, blank=True)