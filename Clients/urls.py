# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.urls import path
from .views import creer_message

# -- définition des urls de l'application Equipement -- #
urlpatterns = [
    path('creer_message/', creer_message, name = "creer_message"),
]