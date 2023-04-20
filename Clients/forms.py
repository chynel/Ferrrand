from django import forms
from Clients.models import Message
from django.contrib.auth import get_user_model


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

    """def save(self, user, commit=True):
        message = super(MessageForm, self).save(commit=False)
        message.idUser = user.id
        if commit:
            message.save()
        return message"""


