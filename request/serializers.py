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
    request = ServiceRequestSerializer(many=True, read_only=True)
    staff = StaffSerializer(many=True, read_only=True)
    class Meta:
        model = models.ServiceRequest
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    request = ServiceRequestSerializer(many=True, read_only=True)
    class Meta:
        model = models.Feedback
        fields = '__all__'