import profile
import django.contrib.staticfiles
from django.forms import forms 
from django.views.generic import TemplateView
from .forms import ChangeProfileProdutorForms, FillProfileForms
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User
from django.shortcuts import get_object_or_404
from pages.forms import *
from pages.choices import *

class HomePageView(TemplateView):
    template_name = "home.html"

@login_required
def Changeprofileview(request):
    myuser = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':

        if myuser.TypeUser == 1:
            form = ChangeProfileProdutorForms(request.POST)
        elif myuser.TypeUser == 2:
            form = ChangeProfileTransportadorForms(request.POST)
        elif myuser.TypeUser == 3:
            form = ChangeProfileProcessadorForms(request.POST)
        else :
            form = ChangeProfileConsumidorForms(request.POST)
                # Check if the form is valid:
        if form.is_valid():
            if myuser.TypeUser == 1:
                myuser.organic_numb_certification = form.cleaned_data['organic_numb_certification']
                myuser.CNPJ = form.cleaned_data['CNPJ']
                myuser.profile_set = True
                myuser.city = form.cleaned_data['city']
                myuser.first_name = form.cleaned_data['first_name']
                myuser.last_name = form.cleaned_data['last_name']
                myuser.state = form.cleaned_data['state']
                myuser.country = form.cleaned_data['country']
                myuser.birthday = form.cleaned_data['birthday']
                
                myuser.save()
            
            return HttpResponseRedirect('/main/')
    # If this is a GET (or any other method) create the default form.
    else:
        # myuser = get_object_or_404(User, pk=request.user.id)
        if myuser.TypeUser == 1:
            form = ChangeProfileProdutorForms()
        elif myuser.TypeUser == 2:
            form = ChangeProfileTransportadorForms()
        elif myuser.TypeUser == 3:
            form = ChangeProfileProcessadorForms()
        else :
            form = ChangeProfileConsumidorForms()

    context = {
        'form': form,
    }
    return render(request,'changeprofile.html', {
        'form': form,
    })

@login_required
def ProfileView(request):
    user = User
    return render(request,"account/profile.html",{'User': User,})

def CreatorView(request):
    user = User
    return render(request,"creator.html",{'User': User,})

class ConsumidorView(TemplateView):
    template_name = "consumidor.html"

class MainView(TemplateView):
    template_name = "main.html"

def how(request):
    user = User
    return render(request,"main.html",{'User': User,})

def EndUserView(request):
    user = User
    return render(request,"enduser.html",{'User': User,})  

