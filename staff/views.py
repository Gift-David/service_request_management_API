from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.

class StaffCreateAPIView(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffUpdateAPIView(generics.UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

# To retrieve a particular staff
class StaffRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDestroyAPIView(generics.DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
