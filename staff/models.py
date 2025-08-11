from django.db import models
from account.models import CustomUser

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)