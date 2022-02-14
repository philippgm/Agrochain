from ast import Delete
from pickle import TRUE
from pyexpat import model
from django.db import models
from users.models import User
from pages.choices import type_transactions

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    # token = models.CharField(unique=True ,max_length=255,primary_key= True)
    # user =models.ForeignKey(User,on_delete=models.CASCADE)
    # type_transaction = models.PositiveIntegerField(choices=type_transactions)

class Anunciar(models.Model):
    timestamp = models.DateTimeField(auto_now=True)


class Checkout(models.Model):
    timestamp = models.DateTimeField(auto_now=True)


class Checkin(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

class Vender(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

class Comprar(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

class Consultar(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
