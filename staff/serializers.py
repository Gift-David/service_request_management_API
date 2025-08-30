from rest_framework import serializers
from .models import Staff
from account.models import CustomUser
from account.serializers import CustomUserSerializer

class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=False)
    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save()
        staff_instance = Staff.objects.create(user=user_instance, **validated_data)
