from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Owner
from .models import School, Level, Exam

class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ['email', 'first_name',  'last_name', 'phone_number', 'adress',]

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['name','city','Neighborhood','type','teaching_type',
                  'description','images','videos','views_number']
        
class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = ['name','prix_pension']

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['name','type','series','taux_reussite']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Adresse Email')
