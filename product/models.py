from ast import For
from enum import auto
from django.db import models
from users.models import Produtor
from django.urls import reverse
from django.views.generic import DetailView


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    produtor = models.ForeignKey(Produtor,null=True,on_delete=models.CASCADE)
    # transportador = models.ForeignKey(Transportador,null=True, on_delete=models.CASCADE)
    # processador = models.ForeignKey(Processador,null=True,on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=30)
    quantidade = models.IntegerField(default=0)
    descricao = models.TextField(blank=True)
    datafabricacao = models.DateField(auto_now=True,null=True)
    tempovalidade = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("product:showproductinfo", kwargs={"id": self.id})

    
