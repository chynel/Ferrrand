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
    sujet = models.CharField(max_length=75, null=False)
    message = models.TextField(null=False)
    dateEnvoi = models.DateTimeField(auto_now=True, null=False)
    reponse = models.TextField(null=False, default="Vous n'avez pas encore de réponse à ce message")
    repondu = models.BooleanField(default=False) # champ pour le drapeau de modification de la reponse par defaut
    idUser = models.ForeignKey(User, verbose_name='Mail Client', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.sujet
    
    def save(self, *args, **kwargs):
        if self.pk:
            # vérifier si le champ reponse a été modifié
            if self.reponse != Message.objects.get(pk=self.pk).reponse:
                self.repondu = True
        super(Message, self).save(*args, **kwargs)
    


class Reservation(models.Model):
    numeroRes = models.CharField(max_length=80, primary_key=True, editable=False, verbose_name='Numéro de réservation généné automatiquement')
    dateReservation = models.DateField(verbose_name='Date de réservation')
    heureReservation = models.TimeField(verbose_name='Heure de réservation')
    idUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Utilisateur')
    idService = models.ForeignKey(Service, on_delete=models.DO_NOTHING, verbose_name='Service')

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




class Commande (models.Model):
    numeroCom = models.CharField(max_length=80, primary_key=True, editable=False, verbose_name='Numero de Commande Généré automatiquement')
    montantCom = models.DecimalField(max_digits=10, verbose_name='Total Facture', decimal_places=2)
    dateCreationCom = models.DateTimeField(verbose_name='Date de création')
    etatCommande = models.BooleanField(default=False, verbose_name='Etat de la commande')
    nombreProduit = models.IntegerField(verbose_name='Nombre de produit total Commander')
    idUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Email Cleint')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.numeroCom = self.generate_random_number()
        super().save(*args, **kwargs)

    def generate_random_number(self):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(8)) + '-' + ''.join(random.choice(string.digits) for i in range(8))
    
    class Meta:
        verbose_name = 'Commande'
        verbose_name_plural = 'Commande'
    
    def __str__(self):
        return self.numeroCom



    

class Facture(models.Model):
    numeroFact = models.CharField(max_length=80, primary_key=True, editable=False, verbose_name='Numero de Facture Généré automatiquement')
    totalFact = models.DecimalField(max_digits=10, verbose_name='Total Facture', decimal_places=2)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    etatFact = models.BooleanField(default=False, verbose_name='Etat Facture')
    numeroResv = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING, verbose_name='Numéro de réservation')
    numeroCom = models.OneToOneField(Commande, on_delete=models.DO_NOTHING, verbose_name='Numéro de commande')
    idUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Email Cleint')

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



class CommanderProduit(models.Model):

    idUser = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='Email Cleint')
    numeroCom = models.OneToOneField(Commande, on_delete=models.DO_NOTHING, verbose_name='Numéro de commande')

    class Meta:
        verbose_name = 'CommanderProduit'
        verbose_name_plural = 'CommanderProduit'

    def __str__(self):
        pass
    
    
    
class Produit(models.Model):
    '''Model definition pour Produit.'''
    libellePro = models.CharField(max_length=80, verbose_name='Libelle Produit')
    prixPro = models.DecimalField(max_digits=10, verbose_name='Prix Produit', decimal_places=2)
    QteProduit = models.IntegerField(verbose_name='Quantité de produit')
    descriptionPro = models.TextField(verbose_name='Description', max_length=1500, null=False)
    photoProduit = models.ImageField(upload_to='photoProduit', default='default.jpg', blank=True)
    dateCreationPro = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')

    class Meta:
        '''Meta definition pour Produit.'''

        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return str(self.libelle)
    
    
    
class Composer(models.Model):
    '''Model definition pour Composer.'''
    idProduit = models.OneToOneField(Produit, on_delete=models.DO_NOTHING, verbose_name='ID Produit')
    idCategorie = models.OneToOneField(Commande, on_delete=models.DO_NOTHING, verbose_name='ID Catégorie')

    class Meta:
        '''Meta definition pour Composer.'''

        verbose_name = 'Composer'
        verbose_name_plural = 'Composers'

    

class CategorieProd(models.Model):
    '''Model definition puor CategorieProd.'''
    libelleCategorie = models.CharField(max_length=80, verbose_name='Libelle Catégorie')

    class Meta:
        '''Meta definition pour CategorieProd.'''

        verbose_name = 'CategorieProd'
        verbose_name_plural = 'CategorieProds'
    
    def __str__(self):
        return str(self.libelleCategorie)