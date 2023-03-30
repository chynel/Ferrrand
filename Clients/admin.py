# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .models import Message
    
    
# -- mise en place des registres -- #
admin.site.register(Message)
