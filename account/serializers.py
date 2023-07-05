from rest_framework import serializers
from .models import User, Otp_base

        
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data.get('email'),
            # otp = validated_data.get('otp'),
            # expire_time = validated_data.get('expire_time')
        )
        user.save()

        return user

class Otp_baseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp_base
        field = ['email', 'otp']