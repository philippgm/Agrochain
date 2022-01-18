from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    Relation = (("Produtor",1),("Consumidor",2),("Transportador",3),("Processador",4),)
    TypeUser = forms.ChoiceField(label='Category', widget=forms.Select, choices=Relation)
    

class ProfileProdutor(User):
    Empresa = models.CharField(max_length=150, blank=False)
    license = models.CharField(max_length=150, blank=False)
    EmpresaCNPJ = models.CharField(max_length=150, blank=False)

class ProfileConsumidor(User):
    pass

class ProfileTransportador(User):
    Empresa = models.CharField(max_length=150, blank=False)
    EmpresaCNPJ = models.CharField(max_length=150, blank=False)
    pass

class ProfileProcessador(User):
    Empresa = models.CharField(max_length=150, blank=False)
    EmpresaCNPJ = models.CharField(max_length=150, blank=False)

    pass

