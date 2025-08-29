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

        return staff_instance
    
    # def update(self, instance, validated_data):
    #     # Check if the username is being updated and if it's the same as the current one
    #     if 'username' in validated_data and instance.username == validated_data['username']:
    #         # If the username hasn't changed, remove it from the validated data
    #         # to prevent the unique constraint from being checked.
    #         del validated_data['username']

    #     # Call the parent update method to handle the rest of the fields
    #     return super().update(instance, validated_data)

