from django.contrib.auth import forms as allauth_forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from pages.choices import *
from users.models import User

# @login_required(login_url='/accounts/login')
class FillProfileForms(forms.Form):
        # TypeUser = forms.ChoiceField(label ="Categoria",choices=Relation)
        company_name = forms.CharField(label ='Empresa',max_length=30)
        CNPJ = forms.CharField(label ='CNPJ', max_length=30)
        organic_numb_certification = forms.CharField(label ='N°certificado',max_length=30)
        first_name = forms.CharField(label ='Nome',max_length=30)
        last_name = forms.CharField(label ='Sobrenome',max_length=30)
        city = forms.CharField(label ='Cidade',max_length=30)
        state  = forms.CharField(label ='Estado',max_length=30)
        country = forms.CharField(label ='Pais',max_length=30)
        birthday = forms.DateField(label = 'Data de Nascimento')
