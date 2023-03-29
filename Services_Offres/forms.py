#coding: utf-8

from django import forms
from .models import Service, Offer

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class OfferForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Offer
        fields = '__all__'