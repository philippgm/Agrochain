from django.contrib.auth import forms as allauth_forms
from django.forms import ModelForm
from django import forms

from .models import User

class UserChangeForm(allauth_forms.UserChangeForm):
    class Meta(allauth_forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(allauth_forms.UserCreationForm):
    class Meta(allauth_forms.UserCreationForm.Meta):
        model = User

class SignupForm(forms.Form):
    # Relation = (("Produtor",1),("Consumidor",2),("Transportador",3),("Processador",4),)
    # Relation = (("Produtor"),("Consumidor"),("Transportador"),("Processador"),)
    Relation = (("1","Produtor"),("2","Consumidor"),("3","Transportador"),(4,"Processador"),)
    TypeUser = forms.ChoiceField(label='Categoria', widget=forms.Select, choices=Relation)

    def signup(self, request, User):
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        User.save()