from django.db import models
from client.models import Client
from staff.models import Staff
from django.core.validators import MaxValueValidator
from datetime import date

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),

    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class RequestNote(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, blank=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
