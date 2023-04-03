from django.db import models
from customers import models as cust
from providers import models as pr

class DocumentType(models.Model):
    type_doc= models.CharField(null=False, blank=False, max_length=15)

class Totals(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    amount= models.FloatField(null=False, blank=False)
    gross_amount= models.FloatField(null=False, blank=False)
    iva_amount= models.FloatField(null=False, blank=False)
    neto_amount= models.FloatField(null=False, blank=False)

class DocumentsItems(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    description= models.CharField(null=False, blank=False, max_length=100)
    amount= models.FloatField(null=False, blank=False)
    iva= models.FloatField(null=False, blank=False)
    amount_iva= models.FloatField(null=False, blank=False)
    #c.ctrl= 
    #patente=
    ret= models.FloatField(null=False, blank=False)


class SalesDocument(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    branch= models.CharField(null=False, blank=False, max_length=20)
    document_number= models.CharField(null=False, blank=False, max_length=20)
    ctrl_number= models.CharField(null=False, blank=False, max_length=20)
    issuance_date= models.DateField(null=False, blank=False)
    registration_date= models.DateField(null=False, blank=False)
    state= models.CharField(null=False, blank=False)
    type_record= models.CharField(choices='',null=False, blank=False)
    document_type= models.ForeignKey(DocumentType,null=False, blank=False)
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