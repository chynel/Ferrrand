#coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request, 'Comptes_Utilisateurs/index.html')


def Enregistrer(request):
    return render(request, 'Comptes_Utilisateurs/Enregistrer.html')


def login(request):
    return render(request, 'Comptes_Utilisateurs/login.html')


def logout(request):
    pass