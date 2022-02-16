from ast import For
from enum import auto
from django.db import models
from django.forms import ChoiceField
from users.models import Produtor, Transportador, User
from django.urls import reverse
from django.views.generic import DetailView
from datetime import time


class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    produtor = models.ForeignKey(Produtor,null=True,on_delete=models.CASCADE)
    # transportador = models.ForeignKey(Transportador,null=True, on_delete=models.CASCADE)
    # processador = models.ForeignKey(Processador,null=True,on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=30,default="0")
    descricao = models.TextField(blank=True)
    datafabricacao = models.DateField(auto_now=True,null=True)
    tempovalidade = models.CharField(max_length=30,default="0")
    preço = models.IntegerField(default=0)
    status = models.CharField(max_length=30,default="Anunciado")
    categoria = models.IntegerField(choices=((1,"Primário"),(2,"Secundário"),), default=0)
    subprodutos = models.ForeignKey('self',null=True,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("product:showproductinfo", kwargs={"id": self.id})
    def get_checklist_url(self):
        return reverse("product:checkinproduct", kwargs={"id": self.id})

class TransporteProduto(models.Model):
    produto = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    transportador = models.ForeignKey(Transportador,null=True,on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True)

    def set_data_inicio(self):
        self.data_inicio = time().strftime("%Y-%m-%d")
        self.save()
        return
    def set_data_fim(self):
        self.data_fim = time().strftime("%Y-%m-%d")
        self.save()
        return
    def Data_inicio(self):
        return self.data_inicio
    def Data_fim(self):
        return self.data_fim

class Compra(models.Model):
    comprador = models.ForeignKey(User,null=False,on_delete=models.CASCADE,related_name="compra_comprador")
    vendedor = models.ForeignKey(User,null=False,on_delete=models.CASCADE,related_name="compra_vendedor")
    produto = models.ForeignKey(Product,null=False,on_delete=models.CASCADE)