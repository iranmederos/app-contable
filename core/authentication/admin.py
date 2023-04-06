from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, CustomUser
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ("id","rol")

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "email")

admin.site.register(Role, RoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
