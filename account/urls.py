from django.urls import path
from .views import get_email_from_user, verify_code


urlpatterns = [
    path('email/',get_email_from_user),
    path('otp/',verify_code)

]