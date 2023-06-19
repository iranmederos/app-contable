from django.db import models
from customers import models as cust
from providers import models as pr
from tax_machine import models as tm

TYPE_RECORD = (("1", "Registro"), ("2", "Complemeto"),
               ("3", "Anulación"), ("4", "Ajuste"))


class DocumentType(models.Model):
    type_doc = models.CharField(null=False, blank=False, max_length=15)

    class Meta:
        verbose_name = ("Document type")
        verbose_name_plural = ("Documents type")

    def __str__(self) -> str:
        return self.type_doc


class SaleDocument(models.Model):
    branch = models.CharField(null=False, blank=False, max_length=20)
    document_number = models.CharField(null=False, blank=False, max_length=20)
    ctrl_number = models.CharField(null=False, blank=False, max_length=20)
    issuance_date = models.DateField(null=False, blank=False)
    registration_date = models.DateField(null=False, blank=False)
    type_record = models.CharField(
        choices=TYPE_RECORD, null=False, blank=False, max_length=20)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.DO_NOTHING, null=False, blank=False)
    customer_code = models.ForeignKey(
        cust.Customer, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = ("Sale document")
        verbose_name_plural = ("Sale documents")

    def __str__(self) -> str:
        return self.document_number


class PurchaseDocument(models.Model):
    branch = models.CharField(null=False, blank=False, max_length=20)
    document_number = models.CharField(null=False, blank=False, max_length=20)
    ctrl_number = models.CharField(null=False, blank=False, max_length=20)
    issuance_date = models.DateField(null=False, blank=False, max_length=20)
    registration_date = models.DateField(null=False, blank=False)
    type_record = models.CharField(
        choices=TYPE_RECORD, null=False, blank=False, max_length=20)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.DO_NOTHING, null=False, blank=False)
    provider_code = models.ForeignKey(
        pr.Provider, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = ("Purchase document")
        verbose_name_plural = ("Purchasing documents")

    def __str__(self) -> str:
        return self.document_number


class SaleSummary(models.Model):
    code = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=False, blank=False, max_length=50)
    n_invoice = models.CharField(null=False, blank=False, max_length=20)
    zeta = models.CharField(null=False, blank=False, max_length=20)
    since = models.DateField(null=False, blank=False)
    until = models.DateField(null=False, blank=False)
    machine = models.ForeignKey(
        tm.TaxMachine, default=None, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Sale summary")
        verbose_name_plural = ("Sales summaries")

    def __str__(self) -> str:
        return self.code


class ItemDocument(models.Model):
    description = models.CharField(null=True, blank=True, max_length=100)
    amount = models.FloatField(null=False, blank=False)
    iva = models.FloatField(null=False, blank=False)
    amount_iva = models.FloatField(null=False, blank=False)
    c_ctrl = models.FloatField(null=True, blank=True)
    patente = models.FloatField(null=True, blank=True)
    ret = models.FloatField(null=True, blank=True)
    sale_document = models.ForeignKey(
        SaleDocument, on_delete=models.CASCADE, null=True, blank=True)
    purchase_document = models.ForeignKey(
       PurchaseDocument, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Item document")
        verbose_name_plural = ("Items documents")

    def __str__(self) -> str:
        return self.description


class RetIVA(models.Model):
    nro_ret = models.CharField(null=True, blank=True, max_length=30)
    date_reception = models.DateField(null=True, blank=True)
    date_ret_iva = models.DateField(null=True, blank=True)
    amount_iva= models.FloatField(null=True, blank=True)
    percent_iva= models.FloatField(null=True, blank=True)
    amount_ret_iva=models.FloatField(null=True, blank=True)
    purchasebonate_accountant= models.CharField(null=True, blank=True, max_length=20)
    purchasebonate_date= models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = ("Retention IVA")
        verbose_name_plural = ("Retentions IVA")

    def __str__(self):
        return self.nro_ret
