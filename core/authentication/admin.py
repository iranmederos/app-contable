from django.contrib import admin
from .models import Role, User
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ("id","rol")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "email")

admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
