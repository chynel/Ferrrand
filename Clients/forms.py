from django import forms
from Comptes_Utilisateurs.forms import CustomUserCreationForm
from .models import Client
from django.core.exceptions import ValidationError
from Comptes_Utilisateurs.models import CustomUser

class ClientForm(forms.ModelForm):
    # Ajout du champ email pour la création du compte utilisateur
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['nom', 'prenoms']

    def save(self, commit=True):
        # Création du compte utilisateur
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("L'adresse e-mail est requise.")
        nom = email.split('@')[0]  # Utilisation de l'adresse email comme nom d'utilisateur
        password = CustomUser.objects.make_random_password()  # Génération d'un mot de passe aléatoire
        util = CustomUser.objects.create_user(email=email, password=password)

        # Création du client avec le compte utilisateur créé
        client = super(ClientForm, self).save(commit=False)
        client.util = util
        if commit:
            client.save()
        return client
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Cette adresse e-mail est déjà utilisée.")
        return email
    
class ClientCreationForm(forms.ModelForm):
    util = CustomUserCreationForm()
    
    class Meta:
        model = Client
        fields = ('nom', 'prenoms', 'util')
        
    def save(self, commit=True):
        util = self.cleaned_data.get('util')
        util = util.save(commit=False)
        client = super().save(commit=False)
        client.util = util
        if commit:
            util.save()
            client.save()
        return client