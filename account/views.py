from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializers import CreateUserOtpSerializer, TokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import User, Otp_base
from .utils import generate_otp, is_valid_otp

from rest_framework.views import APIView
# # Create your views here.


@api_view(['POST'])
def get_email_from_user(request):
    email = request.data.get('email')
    serializer = CreateUserOtpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        otp, expire_time = generate_otp() # generation de l'otp
        email_body = f'''<h1>{otp}</h1>'''
        send_mail('Verifier votre email', email_body,settings.EMAIL_HOST_USER,[email,])
        otp_creation = Otp_base.objects.create(email=email, otp=otp, expire_time=expire_time)
        otp_creation.save()
        return Response("Code envoyé à votre adresse email !")


@api_view(['POST'])
def verify_code(request):
    
    email = request.data.get('email')
    code_to_verify = request.data.get('otp')
    
    try:
        otp_genereted = Otp_base.objects.get(email=email)
    except Otp_base.DoesNotExist:
        return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

    is_valid = is_valid_otp(code_to_verify, str(otp_genereted.otp), otp_genereted.expire_time)
    if is_valid:
        user = User.objects.get(email=email)
        refresh = RefreshToken.for_user(user)
        serializer = TokenSerializer(data={'access': str(refresh.access_token), 'refresh': str(refresh)})
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
        # return Response("Email Vérifié")
    else:
        return Response("Probleme avec l'adresse email ou expiration du code de vérification")


class Login(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        refresh = RefreshToken.for_user(user)
        serializer = TokenSerializer(data={'access': str(refresh.access_token), 'refresh': str(refresh)})
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)