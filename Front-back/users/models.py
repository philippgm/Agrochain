import profile
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from pages.choices import *

class User(AbstractUser):

    TypeUser = models.IntegerField(choices=Relation, default=0)    
    CNPJ = models.CharField(max_length=30, blank=True)
    organic_numb_certification = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=30, blank=True)
    profile_set = models.BooleanField(default = False)
    city = models.CharField(max_length=30, blank=True)
    state  = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(auto_now=True)