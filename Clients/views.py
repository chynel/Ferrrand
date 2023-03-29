# -- encodage du fichier -- #
#coding: utf-8

# -- importations des modules -- #
from django.shortcuts import get_object_or_404, render
from Equipement.models import Equipement
from .models import Client, Message
from django.contrib import messages

"""# -- définition des vues de l'application accueil -- #
def accueil(request):
    # -- recuperation des équipements -- #
    listeEquipements = Equipement.objects.order_by('-datePublication')[:4]

    # -- retourne le template index.html -- #
    return render(request, 'index.html', {'listeEquipements' : listeEquipements})

def contacter(request):
    # -- vérification de request -- #
    if request.method == "POST":
        # -- mise en place de la liste de données -- #
        listeDonnees = [request.POST.get('nom'), request.POST.get('tel'), request.POST.get('email'), request.POST.get('sujet'), request.POST.get('message')]
        
        try:
            # -- recuperation d'un internaute -- #
            clientExistant = Clients.objects.get(nom = listeDonnees[0], numeroTelephone = listeDonnees[1], adresseMail = listeDonnees[2])
        
            # -- vérification -- #
            if clientExistant.nom == listeDonnees[0]:
                # -- sauvegarde du message -- #
                message = Messages(sujet = listeDonnees[3], message = listeDonnees[4], idClients = clientExistant)
                message.save()

                # -- renvoi un message de succès -- #
                messages.success(request, "Votre message a été envoyer avec succès !!")
            else:
                # -- sauvegarde du message et du client -- #
                client = Clients(nom = listeDonnees[0], numeroTelephone = listeDonnees[1], adresseMail = listeDonnees[2])
                client.save()

                message = Messages(sujet = listeDonnees[3], message = listeDonnees[4], idclient = client)
                message.save()

                # -- renvoi un message de succès -- #
                messages.success(request, "Votre message a été envoyer avec succès !!")
        except:
            # -- sauvegarde du message et du client -- #
            client = Clients(nom = listeDonnees[0], numeroTelephone = listeDonnees[1], adresseMail = listeDonnees[2])
            client.save()

            message = Messages(sujet = listeDonnees[3], message = listeDonnees[4], idClients = client)
            message.save()

            # -- renvoi un message de succès -- #
            messages.success(request, "Votre message a été envoyer avec succès !!")

        # -- retourne le template contacter.html -- #
        return render(request, 'contacter.html')
    else:
        # -- retourne le template contacter.html -- #
        return render(request, 'contacter.html')"""