# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.contrib import admin
from .models import Message, Facture, Reservation, Commande
from django.contrib.auth.models import Permission, Group
from .models import Produit, CategorieProd
    
    

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'idUser', 'message', 'reponse', 'repondu') # afficher la colonne modification
    search_fields = ('idUser__email', 'sujet')
    fields = ('sujet', 'message', 'idUser', 'reponse',) # ajouter modification aux fields
    readonly_fields = ('sujet', 'message', 'idUser',)

    

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


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('numeroCom', 'idUser', 'montantCom', 'dateCreationCom', 'etatCommande','nombreProduit',)
    readonly_fields = ('numeroCom',)
    search_fields = ('idUser__email', 'numeroCom',)
    ordering = ('-dateCreationCom',)#Pour que les Factures s'affichent du plus recent à la plus vielle.


class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1
    
class CategorieProdAdmin(admin.ModelAdmin):
    inlines = [ProduitInline]
    

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libellePro', 'prixPro', 'QteProduit', 'categorie',)
    search_fields = ('libellePro', 'descriptionPro',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'categorie':
            kwargs['queryset'] = CategorieProd.objects.filter()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# -- mise en place des registres -- #

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(CategorieProd, CategorieProdAdmin)


admin.site.register(Facture, FactureAdmin)
admin.site.register(Commande, CommandeAdmin)

