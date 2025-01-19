from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import OwnerCreationForm

def register(request):
    if request.method == 'POST':
        form = OwnerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie.")
            return redirect('Book_list')  
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = OwnerCreationForm()
    return render(request, 'schools/register.html', {'form': form})

