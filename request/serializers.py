from rest_framework import serializers
from . import models

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceRequest
        fields = '__all__'

class RequestNoteSerializer(serializers.ModelSerializer):
    request = ServiceRequestSerializer(many=True, read_only=True)
    class Meta:
        model = models.ServiceRequest
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'