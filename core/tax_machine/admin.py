from django.contrib import admin
from .models import TaxMachine
# Register your models here.


class TaxMachineAdmin(admin.ModelAdmin):
    list_display = ("id","brand", "type_machine")

admin.site.register(TaxMachine, TaxMachineAdmin)