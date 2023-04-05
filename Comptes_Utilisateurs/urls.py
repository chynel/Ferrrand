
from django.urls import path
from Comptes_Utilisateurs import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Enregistrer', views.Enregistrer, name='Enregistrer'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout_view'),
    path('profile', views.profile, name='profile')
]