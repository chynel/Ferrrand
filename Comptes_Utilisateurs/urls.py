from django.urls import path
from Comptes_Utilisateurs import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Enregistrer', views.Enregistrer, name='Enregistrer'),
    path('login', views.connexion, name='connexion'),
    path('logout', views.logout_view, name='logout_view'),
]