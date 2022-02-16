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
            userProdutor = Produtor.objects.create(user = myuser)
            produto = Product.objects.create(produtor = userProdutor)
            
            # produto.produtor = 
            produto.quantidade = form.cleaned_data["quantidade"]
            produto.descricao = form.cleaned_data["descricao"]
            produto.datafabricacao = form.cleaned_data["datafabricacao"]
            produto.tempovalidade = form.cleaned_data["tempovalidade"]
            produto.tipo = form.cleaned_data["tipo"]
            produto.preco = form.cleaned_data["preco"]
            produto.status = "Vendido"
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

            if aux == 1:
                a = Product.objects.filter(tipo=aux2)
                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 2:
                a = Product.objects.filter(produtor__user__first_name=aux2)
                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 3:
    
                aux2 = datetime.strptime(aux2,"%d/%m/%Y").strftime("%Y-%m-%d")
                print(aux2)
                a = Product.objects.filter(data_criacao =aux2)

                if len(a) == 0:
                    return render(request,"pesquisarproduto.html",{'Result': None,
                                            "form": form})
            return render(request,"pesquisarproduto.html",{'Result': a,
                                            "form": form})

    else:
        form = PesquisarProdutoForms()
        return render(request,"pesquisarproduto.html",{'User': User,"form": form})

def ShowProductInfoView(request,id):
    a = Product.objects.filter(id=id)
    b = a[0].produtor.user
    c = TransporteProduto.objects.filter(produto__id = id)
    if len(c):
        return render(request,"showproductinfo.html",{"produto":a[0],
                                                    "produtor":b, "transporte":c[0]})
    else:
        return render(request,"showproductinfo.html",{"produto":a[0],
                                                    "produtor":b, })

def CheckinProduct(request):
    if request.method == 'POST':
        form = PesquisarProdutoForms(request.POST)
        if form.is_valid():
            aux = int(form.cleaned_data['tipo_pesquisa'])
            aux2 = form.cleaned_data['pesquisa']

            if aux == 1:
                a = Product.objects.filter(tipo=aux2) & Product.objects.filter(status="Vendido")
                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            elif aux == 2:
                a = Product.objects.filter(produtor__user__first_name=aux2) & Product.objects.filter(status="Vendido")
                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            elif aux == 3:
    
                aux2 = datetime.strptime(aux2,"%d/%m/%Y").strftime("%Y-%m-%d")
                print(aux2)
                a = Product.objects.filter(data_criacao =aux2) & Product.objects.filter(status="Vendido")

                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            return render(request,"checklistproduct.html",{'Result': a,
                                            "form": form})
    else:
        form = PesquisarProdutoForms()
        return render(request,"checklistproduct.html",{'User': User,"form": form})

def CheckinProductView(request,id):
    a = get_object_or_404(Product, pk=id)
    print(a.status)


    trans = Transportador.objects.filter(user__id=request.user.id)
    if ( not len(trans)):
        trans = Transportador.objects.create(user=request.user)
        trans.save()
        TransporteProduto.objects.create(produto = a,transportador=trans[0])
        a.status = "Em Transporte"
        a.save()
        print("Em Transporte")
        return render(request,"transporteproduto.html",{"produto":a[0],})
    transporte = TransporteProduto.objects.create(produto = a,transportador=trans[0])
    a.status = "Em Transporte"
    a.save()
    transporte.set_data_inicio()
    print(transporte.Data_inicio())
    return render(request,"transporteproduto.html",{"produto":a,})

def CheckoutProduct(request):
    if request.method == 'POST':
        form = PesquisarProdutoForms(request.POST)
        if form.is_valid():
            aux = int(form.cleaned_data['tipo_pesquisa'])
            aux2 = form.cleaned_data['pesquisa']

            if aux == 1:
                a = Product.objects.filter(tipo=aux2) & Product.objects.filter(status="Em Transporte")
                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            elif aux == 2:
                a = Product.objects.filter(produtor__user__first_name=aux2) & Product.objects.filter(status="Em Transporte")
                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            elif aux == 3:
    
                aux2 = datetime.strptime(aux2,"%d/%m/%Y").strftime("%Y-%m-%d")
                print(aux2)
                a = Product.objects.filter(data_criacao =aux2) & Product.objects.filter(status="Em Transporte")

                if len(a) == 0:
                    return render(request,"checklistproduct.html",{'Result': None,
                                            "form": form})
            return render(request,"checklistproduct.html",{'Result': a,
                                            "form": form})
    else:
        form = PesquisarProdutoForms()
        return render(request,"checklistproduct.html",{'User': User,"form": form})

def CheckoutProductView(request,id):
    a = get_object_or_404(Product, pk=id)

    if a.status == "Em Transporte":
        a.status = "Entregue"
        a.save()
        transporte = TransporteProduto.objects.filter(produto__id = id)
        transporte.set_data_fim()
    print(transporte.Data_fim())
    return render(request,"transporteproduto.html",{"produto":a,})

def ComprarProdutoView(request,id):
    produto = get_object_or_404(Product, pk=id)
    vendedor = User.objects.filter(produto__id = id)
    print(type(vendedor[0]))
    


def ComprarProduto(request):
    if request.method == 'POST':
        form = PesquisarProdutoForms(request.POST)
        if form.is_valid():
            aux = int(form.cleaned_data['tipo_pesquisa'])
            aux2 = form.cleaned_data['pesquisa']

            if aux == 1:
                a = Product.objects.filter(tipo=aux2) & Product.objects.filter(status="Anunciado")
                if len(a) == 0:
                    return render(request,"comprarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 2:
                a = Product.objects.filter(produtor__user__first_name=aux2) & Product.objects.filter(status="Anunciado")
                if len(a) == 0:
                    return render(request,"comprarproduto.html",{'Result': None,
                                            "form": form})
            elif aux == 3:
    
                aux2 = datetime.strptime(aux2,"%d/%m/%Y").strftime("%Y-%m-%d")
                print(aux2)
                a = Product.objects.filter(data_criacao =aux2) & Product.objects.filter(status="Anunciado")

                if len(a) == 0:
                    return render(request,"comprarproduto.html",{'Result': None,
                                            "form": form})
            return render(request,"comprarproduto.html",{'Result': a,
                                            "form": form})
    else:
        form = PesquisarProdutoForms()
        return render(request,"comprarproduto.html",{'User': User,"form": form})