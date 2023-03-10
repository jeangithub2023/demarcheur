from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    birthday=models.DateField()
    phone=models.IntegerField()
    
    def __str__(self) -> str:
        return self.user.username
    