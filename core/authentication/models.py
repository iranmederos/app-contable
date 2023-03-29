from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE= (('1','Administrador'),('2','Contador'))


class Role(models.Model):
    name = models.CharField(max_length=10,null=False, blank=False,choices=USER_TYPE,default=0)


class CustomUser(AbstractUser):
    user = models.AutoField(null=False, blank=False,primary_key=True, unique=True)
    username =  models.CharField(max_length=50,null=True, blank=True,default=None)
    password = models.CharField(max_length=100,null=False, blank=False)
    first_name = models.CharField(max_length=50,null=False, blank=False)
    last_name =  models.CharField(max_length=50,null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=False, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    rol= models.ForeignKey(Role, blank=False, null=False)
       

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

