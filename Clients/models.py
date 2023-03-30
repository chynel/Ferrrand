# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.db import models
from django.utils import timezone
from Comptes_Utilisateurs.models import CustomUser


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