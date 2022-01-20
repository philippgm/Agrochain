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
        

