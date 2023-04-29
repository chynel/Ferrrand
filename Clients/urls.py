# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.urls import path
from .views import creer_message, supprimer_message, message_reponse
from .views import CategorieProdListView, produit_detail


# -- définition des urls de l'application Equipement -- #
urlpatterns = [
    path('creer_message/', creer_message, name = "creer_message"),
    path('supprimer_message/<int:message_id>/', supprimer_message, name='supprimer_message'),
    path('message_reponse/<int:message_id>/', message_reponse, name='message_reponse'),
    path('produits_cate/', CategorieProdListView.as_view(), name='produits_cate'),
    path('produit/<int:pk>/', produit_detail, name='produit_detail'),
]