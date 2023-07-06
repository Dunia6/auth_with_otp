from django.urls import path
from .views import get_email_from_user, verify_code, Login


urlpatterns = [
    path('register/',get_email_from_user, name="register_user"),
    path('verify_otp/',verify_code, name='verify_otp'),
    path('login/', Login.as_view(), name='login' )
]