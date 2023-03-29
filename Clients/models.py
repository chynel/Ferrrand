# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.db import models
from django.utils import timezone
from Comptes_Utilisateurs.models import CustomUser


# -- définition des classes modèles -- #
class Client(models.Model):
    # -- docstring de la classe Clients -- #
    """
        -- Cette classe représente la table des Clients dans la base de 
        -- Données
    """

    # -- mise en place des attributs de la classe Client -- #
    nom = models.CharField(verbose_name="Nom", max_length = 75, null =  False)
    prenoms = models.CharField(verbose_name="Prenom", max_length = 75, null =  False)
    numeroTelephone = models.CharField(verbose_name="Numero Téléphone", max_length = 75, null = False)
    #adresseMail = models.EmailField(verbose_name="Adresse mail", unique=True)
    dateCreation = models.DateTimeField(verbose_name="Date de création", null = False, default=timezone.now)
    util= models.OneToOneField(CustomUser, verbose_name="Mail User", on_delete=models.CASCADE)
    is_client = models.BooleanField(default=True)
    

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Nom Client : {self.nom} - Date création : {self.prenoms}"


class Message(models.Model):
    # -- docstring de la classe Message -- #
    """
        -- Cette classe représente la table des messages dans la base de 
        -- Données
    """

    # -- mise en place des attributs de la classe messages -- #
    sujet = models.CharField(max_length = 75, null =  False)
    message = models.TextField(null =  False)
    idClient = models.ForeignKey(Client, null = True, on_delete = models.SET_NULL)
    dateEnvoi = models.DateTimeField(auto_now = True, null = False)

    # -- mise en place de la methode __str__ -- #
    def __str__(self):
        return f"Sujet : {self.sujet}" 