from django.db import models
from company import models as comp


class TaxMachine(models.Model):
    TYPE_MACHINE=(("1","Registradora con mem. fiscal"),("2","Impresora fiscal"),("3","Computadora con mem. fiscal"))
    
    type_machine= models.CharField(choices=TYPE_MACHINE, null=False, blank=True, max_length=30)
    serial= models.CharField(null=False, blank=False, max_length=50)
    model= models.CharField(null=True, blank=True, max_length=20)
    brand= models.CharField(null=True, blank=True, max_length=20)
    proveedor= models.CharField(null=True, blank=True, max_length=50)
    company= models.ForeignKey(comp.Company, default=None, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tax machine")
        verbose_name_plural = ("Tax machines")

    def __str__(self) -> str:
        return f"{self.type_machine} - {self.serial}"