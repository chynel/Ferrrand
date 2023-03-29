#coding: utf-8


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
        
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_client', True)
        return self.create_user(email, password, **extra_fields)
    
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    """Variables pour définir les champs du combo sexe"""
    MASCULIN='masculin'
    FEMININ='feminin'
    PAS_DE_SEXE = 'Neutre'
    SEXE=[(MASCULIN,'Masculin'),(FEMININ,'Feminin'),(PAS_DE_SEXE,'Pas de sexe'),]
    
    email = models.EmailField(unique=True)
    noms = models.CharField(verbose_name='Nom(s)', max_length=100, default='Pas de nom(s)')
    prenoms = models.CharField(verbose_name='Prénom(s)', max_length=80, default='Pas de prénom(s)')
    sexe = models.CharField(choices=SEXE, default='Masculin', max_length=8)
    DateNaiss = models.DateField(verbose_name="Date de naissance", default=timezone.now)
    phone = models.CharField(max_length=100, unique=True, null=True)    
    
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    
    
from django.conf import settings
User = settings.AUTH_USER_MODEL