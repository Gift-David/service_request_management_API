from rest_framework import serializers
from .models import Client
from account.serializers import CustomUserSerializer

class ClientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=False)
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save()
        staff_instance = Client.objects.create(user=user_instance, **validated_data)

        return staff_instance