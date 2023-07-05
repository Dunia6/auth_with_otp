from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# # Create your models here.

class User(AbstractUser):
    username = None
    password = None
    email = models.EmailField(_('email address'), unique=True, null=False,blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Otp_base(models.Model):
    email = email = models.EmailField(_('email address'), unique=True, null=False,blank=False)
    otp = models.IntegerField(unique=True,blank=True,null=True)
    expire_time = models.IntegerField(null=True)
    
    def __str__(self):
        return self.email + " " + str(self.otp)