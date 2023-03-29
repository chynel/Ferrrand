#coding: utf-8

from django.db import models

# Create your models here.


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom du service')
    description = models.TextField()

    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de l'ofrre")
    description = models.CharField(max_length=2500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name