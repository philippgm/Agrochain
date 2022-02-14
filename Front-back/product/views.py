import django.contrib.staticfiles
from django.forms import forms 
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import User
from django.shortcuts import get_object_or_404
from .forms import *

@login_required
def CadastrarProdutoView(request):
    if request.method == 'POST':

        
        form = CadastrarProdutoForms(request.POST)
        if form.is_valid():
            myuser = get_object_or_404(User, pk=request.user.id)
            print(type(myuser))
            userProdutor = Produtor.objects.create(userProdutor = myuser)
            produto = Product.objects.create(produtor = userProdutor)
            
            # produto.produtor = 
            produto.quantidade = form.cleaned_data["quantidade"]
            produto.descricao = form.cleaned_data["descricao"]
            produto.datafabricacao = form.cleaned_data["datafabricacao"]
            produto.tempovalidade = form.cleaned_data["tempovalidade"]
            produto.tipo = form.cleaned_data["tipo"]
            produto.save()
            return HttpResponseRedirect('/main/')

    else:
        form = CadastrarProdutoForms()

    context = {
        'form': form,
    }

    return render(request,'cadastraproduto.html', {
        'form': form,
    })
def PesquisarProdutoView(request):
    user = User
    a = Product.objects.filter(tipo="Laranja")
    for i in a:
        print(i.data_criacao)

    return render(request,"pesquisarproduto.html",{'User': User,
                                            'Result': a})
    