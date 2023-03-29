#coding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField



"""class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))"""
    
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password')
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("L'adresse email est déjà utilisée.")
        return email
    
    
class UserAdminChangeForm(forms.ModelForm):
    """
    Un formulaire pour mettre à jour les utilisateurs. Inclut tous les champs sur
    l'utilisateur, mais remplace le champ du mot de passe par celui de l'administrateur
    champ d'affichage du hachage du mot de passe.
    """
    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'is_active', 'is_superuser']
        
    def clean_password(self):
    # Indépendamment de ce que l'utilisateur fournit, renvoie la valeur initiale.
    # Cela se fait ici, plutôt que sur le terrain, car le
    # le champ n'a pas accès à la valeur initiale
        return self.initial["password1"]
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("L'adresse email est déjà utilisée.")
        return email