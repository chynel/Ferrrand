# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .forms import ClientForm
from .models import Client, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('nom', 'prenoms', 'util', 'is_client')
    
    
# -- mise en place des registres -- #
admin.site.register(Message)
