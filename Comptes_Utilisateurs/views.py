# coding: utf-8

from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

# Créez vos vues ici.

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        email = request.user.email
        message = f"Vous êtes connecté avec l'adresse : {email}"
        button_label = "Se deconnecter"
        button_url = "logout_view"
    else:
        message = "Vous n'êtes plus connecté"
        button_label = ""
        button_url = ""
    return render(request, 'index.html', {'message': message, 'button_label': button_label, 'button_url': button_url})



def Enregistrer(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(email=email):
                messages.info(request, "L'email entrez existe déjà")
                return redirect('Enregistrer')
            else:
                user = User.objects.create_user(email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, 'Votre compte a été créé avec succès')
                return redirect('login')
        else:
            messages.info(request, "Les mots de passe sont différents")

        

    return render(request, 'Enregistrer.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Veuillez revoir vos identifiants')
    return render(request, 'login.html')


def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Vous avez bien été déconnecté')
    return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre compte a été mis à jour !')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)