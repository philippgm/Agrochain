from ast import Delete
from pickle import TRUE
from pyexpat import model
from django.db import models
from users.models import User
from pages.choices import *

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    token = models.CharField(unique=True ,max_length=255,primary_key= True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    type_transaction = models.PositiveIntegerField(choices=type_transactions)