from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserCreationSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from .models import User, Otp_base
from .utils import generate_otp, is_valid_otp
# # Create your views here.


@api_view(['POST'])
def get_email_from_user(request):
    email = request.data.get('email')
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        otp, expire_time = generate_otp() # generation de l'otp
        email_body = f'''<h1>{otp}</h1>'''
        send_mail('Verifier votre email', email_body,settings.EMAIL_HOST_USER,[email,])
        otp_creation = Otp_base.objects.create(email=email, otp=otp, expire_time=expire_time)
        otp_creation.save()
        return Response("Email envoyé")


@api_view(['POST'])
def verify_code(request):
    email = request.data.get('email')
    code_to_verify = request.data.get('otp')
    otp_genereted = Otp_base.objects.get(email=email)
    is_valid = is_valid_otp(code_to_verify, otp_genereted.otp, otp_genereted.expire_time)
    if is_valid:
        return Response("Email Vérifié")
    else:
        return Response("Probleme avec l'adresse email ou expiration du code de verification")
