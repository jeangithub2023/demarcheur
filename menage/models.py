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

class Order(models.Model):
    types=models.CharField(max_length=200, default='NULL')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    service=models.ForeignKey(Services, on_delete=models.CASCADE)
    phone=models.IntegerField()
    adresse=models.CharField(max_length=200)
    ordered_date=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=400 ,blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username