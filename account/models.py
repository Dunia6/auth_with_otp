from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# # Create your models here.

class User(AbstractUser):
    username = None
    password = None
    email = models.EmailField(_('email address'), unique=True, null=False,blank=False)
    otp = models.CharField(max_length=255,unique=True,blank=True,null=True)
    otp_time = models.TimeField(default=timezone.now, null=True)
    expire_time = models.TimeField(default=timezone.now, null=True)
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []