from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from . import serializers
from . import models

'''
CRUD operation for the service requests model
'''
class ServiceRequestCreateAPIView(generics.CreateAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ServiceRequestListAPIView(generics.ListAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

class ServiceRequestUpdateAPIView(generics.UpdateAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

# To retrieve a particular service request
class ServiceRequestRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer
    permission_classes = IsAuthenticated

class ServiceRequestDestroyAPIView(generics.DestroyAPIView):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer
    permission_classes = IsAuthenticated

'''
CRUD operation for the request note model
- Only authorized to staffs
'''
class RequestNoteCreateAPIView(generics.CreateAPIView):
    queryset = models.RequestNote.objects.all()
    serializer_class = serializers.RequestNoteSerializer

class RequestNoteListAPIView(generics.ListAPIView):
    queryset = models.RequestNote.objects.all()
    serializer_class = serializers.RequestNoteSerializer

# To retrieve a particular request note
class RequestNoteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.RequestNote.objects.all()
    serializer_class = serializers.RequestNoteSerializer

# Impliment soft delete
class RequestNoteDestroyAPIView(generics.DestroyAPIView):
    queryset = models.RequestNote.objects.all()
    serializer_class = serializers.RequestNoteSerializer


'''
CRUD operation for the feedback model
- Only authorized to clients
- Clients can only create and delete (soft) feedbacks
'''

class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

class FeedbackListAPIView(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

# To retrieve a particular request note
class FeedbackRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer

# Impliment soft delete
class FeedbackDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer