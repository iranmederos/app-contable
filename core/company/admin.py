from django.contrib import admin
from .models import Company, RegistrationData
# Register your models here.

class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ("id","registration_number")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","business_name", "rif", "email")

admin.site.register(Company, CompanyAdmin)
admin.site.register(RegistrationData, RegistrationDataAdmin)