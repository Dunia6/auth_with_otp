from rest_framework import serializers
from .models import User

        
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            otp = validated_data['otp'],
            otp_time = validated_data['otp_time'],
            expire_time = validated_data['expire_time'],
            password = None
        )
        user.save()

        return user