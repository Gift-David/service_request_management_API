from rest_framework import serializers
from .models import Staff
from account.serializers import CustomUserSerializer

class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=False)
    class Meta:
        model = Staff
        fields = '__all__'