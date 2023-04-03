# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import redirect, render
from Comptes_Utilisateurs.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Créez vos vues ici.


def home(request):
    return render(request, 'Comptes_Utilisateurs/index.html')


def Enregistrer(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        myCustomUser = CustomUser.objects.create_user(email=email, password=password)
        messages.success(request, 'Votre compte a été créé avec succès')
        return redirect('connexion')

    return render(request, 'Comptes_Utilisateurs/Enregistrer.html')


def connexion(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        customUser = authenticate(email=email, password=password)
        if customUser is not None:
            login(request, customUser)
            email = customUser.email
            password = customUser.password
            print(125)
            return render(request, 'Comptes_Utilisateurs/index.html', {'email':email})
        else:
            messages.error(request, 'Veuillez revoir vos identifiants')
    return render(request, 'Comptes_Utilisateurs/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Vous avez bien été déconnecté')
    return redirect('home')
