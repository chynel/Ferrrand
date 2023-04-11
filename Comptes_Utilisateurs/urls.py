
from django.urls import path, re_path
from Comptes_Utilisateurs import views
from .views import login_view, register_user, changpassword, ProfileView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name="home"),
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ProfileView', views.ProfileView, name='ProfileView'),
    path('changpassword/', views.changpassword, name='changpassword'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]