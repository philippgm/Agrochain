from django.contrib.auth import forms as allauth_forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from pages.choices import *

class CadastrarProdutoForms(forms.Form):
    tipo = forms.CharField(label = "Tipo",max_length=30)
    quantidade = forms.IntegerField(label = "Quantidade")
    descricao = forms.CharField(label = "Descrição")
    datafabricacao = forms.DateField(label = "Data de Fabricação")
    tempovalidade = forms.IntegerField(label = "Tempo de validade")

class PesquisarProdutoForms(forms.Form):
    tipo_pesquisa = forms.ChoiceField(label='Pesquisa', widget=forms.Select, choices=tipos_pesquisas)
    pesquisa = forms.CharField(label="Produto")