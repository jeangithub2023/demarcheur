from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Menus(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    
    def __str__(self) -> str:
        return self.name

class Services(models.Model):
    menu=models.ForeignKey(Menus, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    
    def __str__(self) -> str:
        return self.name
