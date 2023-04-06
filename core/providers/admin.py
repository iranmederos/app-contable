from django.contrib import admin
from .models import Provider
# Register your models here.


class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id","business_name", "rif")

admin.site.register(Provider, ProviderAdmin)