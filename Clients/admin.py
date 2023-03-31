# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .models import Message, Facture, Reservation
    
    

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('numeroRes', 'idUser', 'idService', 'dateReservation', 'heureReservation',)
    readonly_fields = ('numeroRes',)
    search_fields = ('idUser__email', 'numeroRes')
    ordering = ('-dateReservation',)#Pour que les Réservations s'affichent du plus recent à la plus vielle.
    

class FactureAdmin(admin.ModelAdmin):
    list_display = ('numeroFact', 'idUser', 'totalFact', 'dateCreation', 'etatFact',)
    readonly_fields = ('numeroFact',)
    search_fields = ('idUser__email', 'numeroFact',)
    ordering = ('-dateCreation',)#Pour que les Factures s'affichent du plus recent à la plus vielle.

# -- mise en place des registres -- #

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Message)
admin.site.register(Facture, FactureAdmin)

