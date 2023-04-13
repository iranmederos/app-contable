from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class Role(models.Model):
    rol = models.CharField(max_length=10,null=False, blank=False)

    def __str__(self) -> str:
        return self.rol

class CustomUser(AbstractUser):
    username =  models.CharField(max_length=50,null=True, blank=True,default=None)
    password = models.CharField(max_length=100,null=False, blank=False)
    first_name = models.CharField(max_length=50,null=False, blank=False)
    last_name =  models.CharField(max_length=50,null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=False, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    rol= models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=True)
       

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password']

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')
