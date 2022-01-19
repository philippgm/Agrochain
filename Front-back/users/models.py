import profile
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    Relation = (("1","Produtor"),("2","Consumidor"),("3","Transportador"),(4,"Processador"),)
    TypeUser = forms.ChoiceField(label='Category', widget=forms.Select, choices=Relation)
    