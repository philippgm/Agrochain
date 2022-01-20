from pyexpat import model
from django.db import models
from users.models import User
class Transation(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = User