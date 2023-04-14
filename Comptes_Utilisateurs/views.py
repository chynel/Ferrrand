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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Profile


# Créez vos vues ici.



User = get_user_model()

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
            quest = form.cleaned_data.get("question")
            rep = form.cleaned_data.get("reponse")
            user = auth.authenticate(email=email, password=raw_password)

            msg = 'Utilisateur créé avec succès.'
            success = True

            # return redirect("/login/")

        else:
            msg = "Le formulaire n'est pas valide"
    else:
        form = SignUpForm()
        
    
    question_choices = User.QUESTION_CHOICES
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success, 'question_choices': question_choices})




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
def ProfileView(request):
    msg = None
    success = False

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            # Vérifier si le numéro de téléphone est unique
            phone_number = profile_form.cleaned_data['phone']
            if User.objects.exclude(pk=request.user.pk).filter(profile__phone=phone_number).exists():
                # Numéro de téléphone déjà utilisé
                msg = 'Ce numéro de téléphone est déjà utilisé.'
            else:
                # Enregistrer les modifications
                if user_form.is_valid():
                    user = user_form.save(commit=False)
                    user.save()
                    profile_form.save()
                    msg = 'Votre compte a été mis à jour !'
                    success = True
                else:
                    msg = 'Veuillez corriger les erreurs ci-dessous.'
        else:
            msg = 'Veuillez corriger les erreurs ci-dessous.'
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {"user_form": user_form, "profile_form": profile_form, "msg": msg, "success": success})



def changpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        question = request.POST.get('question')
        reponse = request.POST.get('reponse')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Vérifier si l'e-mail existe dans la base de données
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Le mail entré n'existe pas. Veuillez réessayer.")
            return redirect('changpassword')

        # Vérifier si la réponse à la question secrète est correcte
        
        if user.question != question or user.reponse != reponse:
            messages.error(request, "La question ou la réponse à la question secrète est incorrecte.")

        # Vérifier si les deux mots de passe correspondent
        if password1 != password2:
            messages.error(request, 'Les deux mots de passe ne correspondent pas.')

        # Réinitialiser le mot de passe
        if not messages.get_messages(request):
            user.set_password(password1)
            user.save()
            messages.success(request, 'Le mot de passe a été réinitialisé avec succès.')

    # Afficher le formulaire de réinitialisation du mot de passe
    question_choices = User.QUESTION_CHOICES
    context = {'question_choices': question_choices}
    for message in messages.get_messages(request):
        context[str(message.level_tag)] = message
    return render(request, 'changpassword.html', context)