from django import forms
from .models import Message
from django.contrib.auth import get_user_model
from .models import Produit, CategorieProd


User = get_user_model()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sujet', 'message']
        
        widgets = {
            'sujet': forms.TextInput(attrs={"placeholder": "Sujet", "class": "form-control"}),
            'message': forms.Textarea(attrs={"placeholder": "Message", "class": "form-control"}),
            'idUser': forms.HiddenInput(),
        }        

class CategorieProdForm(forms.ModelForm):
    class Meta:
        model = CategorieProd
        fields = '__all__'

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
