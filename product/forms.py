from django.contrib.auth import forms as allauth_forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from pages.choices import *

class CadastrarProdutoForms(forms.Form):
    tipo = forms.CharField(label = "Tipo",max_length=30)
    quantidade = forms.CharField(label = "Quantidade (unidade)")
    descricao = forms.CharField(label = "Descrição",widget=forms.Textarea)
    datafabricacao = forms.DateField(label = "Data de Fabricação")
    tempovalidade = forms.CharField(label = "Tempo de validade (dias)")
    preco = forms.IntegerField(label = "Preço (R$)")


class PesquisarProdutoForms(forms.Form):
    tipo_pesquisa = forms.ChoiceField(label='Opção de Pesquisa', widget=forms.Select, choices=tipos_pesquisas)
    pesquisa = forms.CharField(label="Produto")