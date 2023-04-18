from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import MessageForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Message



User = get_user_model()


@login_required
def creer_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.idUser = request.user
            message.dateEnvoi = timezone.now()
            message.save()
            return redirect('messages_liste')
    else:
        form = MessageForm()
    return render(request, 'creer_message.html', {'form': form})

def messages_liste(request):
    if request.method == 'POST' and 'submit' in request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.idUser = request.user
            message.dateEnvoi = timezone.now()
            message.save()
            return redirect('messages_liste')
    else:
        form = MessageForm()

    messages = Message.objects.all()
    context = {'messages': messages, 'form': form}
    return render(request, 'messages_liste.html', context)