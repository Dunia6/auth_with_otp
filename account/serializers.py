from rest_framework import serializers
from .models import User, Otp_base


        
class CreateUserOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',]
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data.get('email'),
        )
        user.save()

        return user


class UserCompleteAccount(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        


class Otp_baseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp_base
        field = ['email', 'otp']


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
