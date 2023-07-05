from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import time
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=False,blank=False)
    otp = models.CharField(max_length=255,unique=True,blank=True,null=True)
    otp_time = models.TimeField(default=time.time)
    expire_time = models.TimeField(default=time.time)
    password = None
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []