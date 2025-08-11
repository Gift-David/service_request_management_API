from django.db import models
from account.models import CustomUser
from django.conf import settings

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

