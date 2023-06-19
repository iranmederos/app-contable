from django.db import models
from django.contrib.auth.models import AbstractUser



class Role(models.Model):
    ADMIN = 'admin'
    USER = 'contador'
    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (USER, 'Contador'),
    ]
    rol = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False, blank=False)

    def __str__(self) -> str:
        return self.rol

class User(AbstractUser):
    username =  models.CharField(max_length=50,null=True, blank=True,default=None)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100,null=False, blank=False)
    first_name = models.CharField(max_length=50,null=False, blank=False)
    last_name =  models.CharField(max_length=50,null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=False, null=True, blank=True)
    rol= models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=True)
       

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']
