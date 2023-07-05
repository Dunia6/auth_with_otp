from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserCreationSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from .models import User
from .utils import generate_otp, is_valid_otp
# # Create your views here.


@api_view(['POST', 'GET'])
def get_email_from_user(request):
    email = request.data.get('email')
    serializer = UserCreationSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        otp, otp_time, expire_time = generate_otp() # generation de l'otp
        email_body = f'''<h1>{otp}</h1>'''
        send_mail('Verifier votre email', email_body,settings.EMAIL_HOST_USER,[email,])
        user = User.objects.get(email=email)
        print(user)
        user.save(commit=False)
        user.otp = otp
        user.otp_time = otp_time
        user.expire_time = expire_time
        
        user.save()
        return Response("Email envoyé")


@api_view(['POST'])
def verify_code(request):
    email = request.data.get('email')
    code = request.data.get('otp')
    user = User.objects.get(email=email)
    if is_valid_otp(user.otp, user.otp_time, user.expire_time):
        return Response("Email Vérifié")
    else:
        return Response("error inserer une bonne adresse")
