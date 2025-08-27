from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# To retrieve a particular client
class ClientRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClientDestroyAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]