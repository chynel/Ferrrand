#coding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


    
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
    
    
    

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'image')
        

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Profile.objects.filter(phone=phone).exists():
            raise forms.ValidationError('Ce numéro est déjà est déjà pris')
        return phone


    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "readonly": True,
            }
        ),
        required=False
    )
    
    noms = forms.CharField(
        label='Nom(s)',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom(s)",
                "class": "form-control"
            }
        ),
        required=False
    )
    
    prenoms = forms.CharField(
        label='Prénom(s)',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Prénom(s)",
                "class": "form-control"
            }
        ),
        required=False
    )
    
    sexe_choices = [('MASCULIN', 'Masculin'), ('FEMININ', 'Féminin'), ('PAS_DE_SEXE', 'Pas de sexe')]
    sexe = forms.ChoiceField(
        choices=sexe_choices, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False)
    
    
    DateNaiss = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date de naissance",
                "class": "form-control"
            }
        ),
        required=False
    )
    

    class Meta:
        model = CustomUser
        fields = ['email', 'noms', 'prenoms','sexe','DateNaiss',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Cet e-mail est déjà utilisé.')
        return email




class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(
        ),
        required=False,
    )

    phone = forms.CharField(
        label='Téléphone',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Téléphone",
                "class": "form-control"
            }
        ),
        required=False,
    )

    class Meta:
        model = Profile
        fields = ['phone', 'image']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Profile.objects.filter(phone=phone).exclude(user=self.instance.user).exists():
            print('Ce numéro de téléphone est déjà utilisé.')
        return phone

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user = self.instance.user

        # enregistrer l'image téléchargée
        image = self.cleaned_data.get('image')
        if image:
            profile.image = image

        if commit:
            profile.save()

        return profile

#Juste pour voir
    
class LoginForm(forms.Form):
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Vérification Mot de passe",
                "class": "form-control"
            }
        ))
      
    question_choices = [('Ville', "Le nom de la ville où vos parents se sont rencontrés"), ('Film', "Le nom de votre film préféré"), ('Marque', "Votre marque de vêtement préférée"), ('Autre', "Autre"),]

    question = forms.CharField(
        widget=forms.Select(choices=question_choices),
        required=True,
    )

    reponse = forms.CharField(
        label='Réponse',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Réponse",
                "class": "form-control"
            }
        ),
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'question', 'reponse')