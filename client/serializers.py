from rest_framework import serializers
from .models import Client
from account.serializers import CustomUserSerializer

class ClientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'