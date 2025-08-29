from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'