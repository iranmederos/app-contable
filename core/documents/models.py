from django.db import models
from customers import models as cust
from providers import models as pr

class DocumentType(models.Model):
    type_doc= models.CharField(null=False, blank=False, max_length=15)

class Totals(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    amount= models.FloatField()
    gross_amount= models.FloatField()
    iva_amount= models.FloatField()
    neto_amount= models.FloatField()

class DocumentsItems(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    description= models.CharField()
    amount= models.FloatField()
    iva= models.FloatField()
    amount_iva= models.FloatField()
    #c.ctrl= 
    #patente=
    ret= models.FloatField()


class SalesDocument(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    branch= models.CharField()
    document_number= models.CharField()
    ctrl_number= models.CharField()
    issuance_date= models.DateField()
    registration_date= models.DateField()
    state= models.CharField()
    type_record= models.CharField(choices='')
    document_type= models.ForeignKey(DocumentType,)
    customer_code= models.ForeignKey(cust.Customer)
    provider_code= models.ForeignKey(pr.Provider)


class BuysDocument(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    branch= models.CharField()
    document_number= models.CharField()
    ctrl_number= models.CharField()
    issuance_date= models.DateField()
    registration_date= models.DateField()
    state= models.CharField()
    type_record= models.CharField(choices='')
    document_type= models.ForeignKey(DocumentType,)
    customer_code= models.ForeignKey(cust.Customer)
    provider_code= models.ForeignKey(pr.Provider)


class SalesSummary(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    code= models.CharField()
    description= models.CharField()
    type= models.CharField(choices='')
    serial= models.CharField()
    model= models.CharField()
    n_invoice= models.CharField()
    zeta= models.CharField()
    #since until