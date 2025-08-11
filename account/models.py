from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('client', 'Client'),
    )

    updated_at = models.DateField(default=timezone.now)
    role = models.CharField(choices=CHOICES)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)