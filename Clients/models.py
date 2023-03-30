# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.db import models
import random
import string
import uuid
from django.utils import timezone
from Comptes_Utilisateurs.models import CustomUser
from Services_Offres.models import Service


from django.conf import settings
User = settings.AUTH_USER_MODEL


class Message(models.Model):
    # -- docstring de la classe Message -- #
    """
        -- Cette classe représente la table des messages dans la base de 
        -- Données
    """

    # -- mise en place des attributs de la classe messages -- #
    sujet = models.CharField(max_length = 75, null =  False)
    message = models.TextField(null =  False)
    idUser = models.ForeignKey(User, verbose_name='Mail Client', null = True, on_delete = models.SET_NULL)
    dateEnvoi = models.DateTimeField(auto_now = True, null = False)

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Sujet : {self.sujet}" 
    
    
class Facture(models.Model):
    # -- docstring de la classe Message -- #
    """
        -- Cette classe représente la table des messages dans la base de 
        -- Données
    """
    
    numeroFact = models.CharField(max_length=10, unique=True)
    totalFact = models.DecimalField(max_digits=10, decimal_places=2)
    dateCreation = models.DateTimeField(auto_now_add=True)
    etatFact = models.BooleanField(default=False)
    #numeroResv = models.ForeignKey(Reservation, null = True, on_delete = models.SET_NULL)
    #numeroCom = models.ForeignKey(Commande, null = True, on_delete = models.SET_NULL)
    idUser = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.numeroFact:
            self.numeroFact = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super().save(*args, **kwargs)


class Reservation(models.Model):
    numeroRes = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateReservation = models.DateField()
    heureReservation = models.TimeField()
    idUser = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    idService = models.ForeignKey(Service, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return str(self.numeroRes)