from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# # Create your models here.

# class User(AbstractUser):
#     username = None
#     password = None
#     email = models.EmailField(_('email address'), unique=True, null=False,blank=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Otp_base(models.Model):
    email = email = models.EmailField(
        _('email address'), 
        unique=True, 
        null=False,
        blank=False
    )
    otp = models.IntegerField(
        unique=True,
        blank=True,
        null=True
    )
    expire_time = models.IntegerField(
        null=True
    )
    
    def __str__(self):
        return self.email + " " + str(self.otp)



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Crée et enregistre un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Crée et enregistre un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField(_("Mot de passe"), max_length=50, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.

    def get_full_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.admin
    
    
    def get_short_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "L'utilisateur a-t-il une autorisation spécifique ?"
        # Réponse la plus simple possible : Oui, toujours
        return True

    def has_module_perms(self, app_label):
        "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application `app_label`?"
        return self.is_superuser