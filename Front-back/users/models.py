import profile
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    Relation = (("Produtor",1),("Consumidor",2),("Transportador",3),("Processador",4),)
    TypeUser = forms.ChoiceField(label='Category', widget=forms.Select, choices=Relation)
    
    