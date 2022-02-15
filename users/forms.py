from django.contrib.auth import forms as allauth_forms
from django.forms import ModelForm, fields, widgets
from django import forms
from pages.choices import *

from .models import Consumidor, Processador, Produtor, Transportador, User

class UserChangeForm(allauth_forms.UserChangeForm):
    class Meta(allauth_forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(allauth_forms.UserCreationForm):
    class Meta(allauth_forms.UserCreationForm.Meta):
        model = User

class SignupForm(forms.Form):
    TypeUser = forms.ChoiceField(label='Categoria', widget=forms.Select, choices=Relation)
    def signup(self, request, user):
        user.TypeUser = self.cleaned_data['TypeUser']
        if user.TypeUser == 1:
            Produtor.objects.create(userProdutor = user)
        elif user.TypeUser == 2:
            Consumidor.objects.create(userProdutor = user)
        elif user.TypeUser == 3:
            Transportador.objects.create(userProdutor = user)
        else:
            Processador.objects.create(userProdutor = user)
        user.save()

