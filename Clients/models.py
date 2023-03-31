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


class Reservation(models.Model):
    numeroRes = models.CharField(max_length=80, primary_key=True, editable=False, verbose_name='Numéro de réservation généné automatiquement')
    dateReservation = models.DateField(verbose_name='Date de réservation')
    heureReservation = models.TimeField(verbose_name='Heure de réservation')
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    idService = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.numeroRes = self.generate_random_number()
        super().save(*args, **kwargs)

    def generate_random_number(self):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(8)) + '-' + ''.join(random.choice(string.digits) for i in range(8))

    def __str__(self):
        return str(self.numeroRes)

    class Meta:
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'

    

class Facture(models.Model):
    numeroFact = models.CharField(max_length=80, primary_key=True, editable=False, verbose_name='Numero de Facture Généré automatiquement')
    totalFact = models.DecimalField(max_digits=10, verbose_name='Total Facture', decimal_places=2)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    etatFact = models.BooleanField(default=False, verbose_name='Etat Facture')
    numeroResv = models.ForeignKey('Reservation', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Numéro de réservation')
    #numeroCom = models.ForeignKey('Commande', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Numéro de commande')
    idUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Email Cleint')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.numeroFact = self.generate_random_number()
        super().save(*args, **kwargs)

    def generate_random_number(self):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(8)) + '-' + ''.join(random.choice(string.digits) for i in range(8))

    def __str__(self):
        return str(self.numeroFact)

    class Meta:
        verbose_name = 'Facture'
        verbose_name_plural = 'Factures'
