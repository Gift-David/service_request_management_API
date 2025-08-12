from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

'''CRUD operation for the service requests model'''
class ServiceRequestCreateAPIView(generics.CreateAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

class ServiceRequestListAPIView(generics.ListAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

class ServiceRequestUpdateAPIView(generics.UpdateAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

# To retrieve a particular service request
class ServiceRequestRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

class ServiceRequestDestroyAPIView(generics.DestroyAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

'''CRUD operation for the request note model'''

'''CRUD operation for the feedback model'''