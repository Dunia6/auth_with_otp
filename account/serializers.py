from rest_framework import serializers
from .models import User

        
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'otp', 'otp_time', 'expire_time']
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data.get('email'),
            otp = validated_data.get('otp'),
            otp_time = validated_data.get('otp_time'),
            expire_time = validated_data.get('expire_time'),
        )
        user.save()

        return user