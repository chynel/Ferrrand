# coding: utf-8

from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .forms import LoginForm, SignUpForm
from django import template
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


# Créez vos vues ici.



User = get_user_model()
"""
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
    
"""

#Juste pour voir

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                msg = "Informations d'identification invalides"
        else:
            msg = 'Erreur lors de la validation du formulaire'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = auth.authenticate(email=email, password=raw_password)

            msg = 'Utilisateur créé avec succès.'
            success = True

            # return redirect("/login/")

        else:
            msg = "Le formulaire n'est pas valide"
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
   # Tous les chemins de ressources se terminent par .html.
   # Choisissez le nom du fichier html à partir de l'url. Et chargez ce modèle.


    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


@login_required(login_url="/login/")
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



def changpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Vérifier si l'e-mail existe dans la base de données
        try:
            user = User.objects.get(email=email)
            profil = User.objects.get(user=user)
        except:
            messages.error(request, 'Une erreur est survenue. Veuillez réessayer.')
            return redirect('changpassword')

        # Vérifier si la réponse à la question secrète est correcte
        if profil.question != question or profil.answer != answer:
            messages.error(request, 'La réponse à la question secrète est incorrecte.')
            return redirect('changpassword')

        # Vérifier si les deux mots de passe correspondent
        if password1 != password2:
            messages.error(request, 'Les deux mots de passe ne correspondent pas.')
            return redirect('changpassword')

        # Réinitialiser le mot de passe
        user.set_password(password1)
        user.save()
        messages.success(request, 'Le mot de passe a été réinitialisé avec succès.')
        return redirect('login')

    # Afficher le formulaire de réinitialisation du mot de passe
    question_choices = User.QUESTION_CHOICES
    return render(request, 'changpassword.html', {'question_choices': question_choices})
