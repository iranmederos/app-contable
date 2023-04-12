from django.db import models



TYPE_MACHINE=(("1","Registradora con mem. fiscal"),("2","Impresora fiscal"),("3","Computadora con mem. fiscal"))

class TaxMachine(models.Model):
    id= models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    type_machine= models.CharField(choices=TYPE_MACHINE)
    serial= models.CharField()
    model= models.CharField()
    brand= models.CharField()
    proveedor= models.CharField()

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self) -> str:
        return f"{self.type_machine} - {self.model}"