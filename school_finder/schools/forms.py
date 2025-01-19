from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Owner

class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ['email', 'first_name',  'last_name', 'phone_number', 'adress',]
