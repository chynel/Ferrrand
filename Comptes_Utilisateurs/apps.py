#coding: utf-8

from django.apps import AppConfig


class ComptesUtilisateursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Comptes_Utilisateurs'
    
    def ready(self):
        import Comptes_Utilisateurs.signals
