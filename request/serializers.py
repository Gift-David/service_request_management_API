from rest_framework import serializers
from . import models
from client.serializers import ClientSerializer
from staff.serializers import StaffSerializer

class ServiceRequestSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(read_only=True)
    staffs = StaffSerializer(many=True, read_only=True)
    class Meta:
        model = models.ServiceRequest
        fields = '__all__'

class RequestNoteSerializer(serializers.ModelSerializer):
    requests = ServiceRequestSerializer(read_only=True)
    staffs = StaffSerializer(read_only=True)
    class Meta:
        model = models.RequestNote
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    requests = ServiceRequestSerializer(many=True, read_only=True)
    class Meta:
        model = models.Feedback
        fields = '__all__'