from unicodedata import name
import django.contrib.staticfiles
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import User
from django.shortcuts import get_object_or_404
from .forms import *
from datetime import date, datetime

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
    # user = User
    # myuser = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        form = PesquisarProdutoForms(request.POST)
        if form.is_valid():
            aux = int(form.cleaned_data['tipo_pesquisa'])
            aux2 = form.cleaned_data['pesquisa']
            print("asdasdasd")
            if aux == 1:
                a = Product.objects.filter(tipo=aux2)
                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 2:
                a = Product.objects.filter(produtor__userProdutor__first_name=aux2)
                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 3:
                # dataFormatada = datetime.strftime(aux2)
                # aux2 = date.strftime('%Y/%m/%d')
                print(aux2)
                a = Product.objects.filter(data_criacao =aux2)

                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            print("fffffff")
            return render(request,"pesquisarproduto.html",{'Result': a,
                                            "form": form})

    else:
        form = PesquisarProdutoForms()
        return render(request,"pesquisarproduto.html",{'User': User,"form": form})

def ShowProductInfoView(request,id):
    a = Product.objects.filter(id=id)
    b = a[0].produtor.userProdutor
    return render(request,"showproductinfo.html",{"produto":a[0],
                                                    "produtor":b})
