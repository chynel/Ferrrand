#coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os


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
    SEXE_CHOICES = [    ('MASCULIN', 'Masculin'),    ('FEMININ', 'Féminin'),    ('PAS_DE_SEXE', 'Pas de sexe'),]
    
    email = models.EmailField(unique=True)
    noms = models.CharField(verbose_name='Nom(s)', max_length=100, default='Pas de nom(s)')
    prenoms = models.CharField(verbose_name='Prénom(s)', max_length=80, default='Pas de prénom(s)')
    sexe = models.CharField(choices=SEXE_CHOICES, max_length=100)
    DateNaiss = models.DateField(verbose_name="Date de naissance", default=timezone.now)
    
    QUESTION_CHOICES = [
            ('Ville', "Le nom de la ville où vos parents se sont rencontrés"),
            ('Film', "Le nom de votre film préféré"),
            ('Marque', "Votre marque de vêtement préférée"),
            ('Autre', "Autre"),
        ]
    question = models.CharField(max_length=100, choices=QUESTION_CHOICES)
    reponse = models.CharField(max_length=100)
    
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    
    
from django.conf import settings
User = settings.AUTH_USER_MODEL
    



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoProfil', default='default.jpg', blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_profile = Profile.objects.get(pk=self.pk)
            if self.image and old_profile.image != self.image:
                default_storage.delete(os.path.join(settings.MEDIA_ROOT, old_profile.image.name))
        if not self.pk:
            self.image = self.compressImage(self.image)
        super(Profile, self).save(*args, **kwargs)

    def compressImage(self, uploaded_image):
        image_temporary = Image.open(uploaded_image)
        output_io_stream = BytesIO()
        image_temporary.save(output_io_stream , format='JPEG', quality=60)
        output_io_stream.seek(0)
        uploaded_image = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % uploaded_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
        return uploaded_image

    def __str__(self):
        return f'{self.user.email} Profile'