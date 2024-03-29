from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import MessageForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Message
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from .models import CategorieProd, Produit
from django.utils.decorators import method_decorator



User = get_user_model()


@login_required
def creer_message(request):
    messages_liste = Message.objects.filter(idUser=request.user).order_by('-id')[:25]
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.idUser = request.user
            
            # Vérifier le nombre de messages déjà enregistrés
            messages_count = Message.objects.filter(idUser=request.user).count()
            if messages_count >= 25:
                messages.warning(request, 'Vous avez 25 messages sur votre liste de messages envoyés, supprimez les plus anciens pour enregistrer de nouveaux.')
                return render(request, 'form_elements.html', {'form': form, 'messages_liste': messages_liste})
            
            message.save()
            messages.success(request, 'Votre message a été envoyé avec succès!')
            form = MessageForm()
        else:
            messages.error(request, 'Une erreur s\'est produite. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = MessageForm(initial={'idUser': request.user})
    
    return render(request, 'form_elements.html', {'form': form, 'messages_liste': messages_liste})



@login_required
def supprimer_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, idUser=request.user)
    message.delete()
    messages.success(request, 'Votre message a été supprimé avec succès.')
    return redirect('creer_message')


@login_required
def message_reponse(request, message_id):
    message = get_object_or_404(Message, id=message_id, idUser=request.user)
    messages_liste = Message.objects.filter(idUser=request.user).order_by('-id')[:25]
    return render(request, 'message_reponse.html', {'message': message, 'messages_liste': messages_liste})


@method_decorator(login_required, name='dispatch')
class CategorieProdListView(ListView):
    model = CategorieProd
    template_name = 'produits_cate.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produits = Produit.objects.all()
        context['produits'] = produits
        return context
    

@login_required
def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    context = {'produit': produit}
    return render(request, 'nom_de_votre_template.html', context)

