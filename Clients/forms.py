from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sujet', 'message', 'idUser']
        
        widgets = {
            'sujet': forms.TextInput(attrs={"placeholder": "Sujet", "class": "form-control"}),
            'message': forms.Textarea(attrs={"placeholder": "Message", "class": "form-control"}),
            'idUser': forms.TextInput(attrs={"placeholder": "ID utilisateur", "class": "form-control"}),
        }