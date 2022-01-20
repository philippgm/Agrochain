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
    profile_set = False
