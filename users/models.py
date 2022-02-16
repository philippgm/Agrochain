import profile
from tkinter import CASCADE
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from pages.choices import *
from django.http import request
from django.shortcuts import render

class User(AbstractUser):

    TypeUser = models.IntegerField(choices=Relation, default=0)    
    CNPJ = models.CharField(max_length=30, blank=True)
    organic_numb_certification = models.CharField(max_length=30, blank=True)
    is_organic = models.BooleanField(default=False)
    company_name = models.CharField(max_length=30, blank=True)
    cargo = models.CharField(max_length=255,blank=True)
    profile_set = models.BooleanField(default = False)
    city = models.CharField(max_length=30, blank=True)
    state  = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(blank=True,null=True)
    # ts = [("Anunciar","Checkout","Checkin","Vender","Comprar","Consultar"),("Checkout","Checkin","Consultar"),("Checkout","Checkin","Consultar"),("Checkout","Checkin","Consultar")]

class Produtor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # transactions = models.ForeignKey(on_delete=models.CASCADE)

class Consumidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Transportador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Processador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   