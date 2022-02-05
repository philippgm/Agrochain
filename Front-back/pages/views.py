import profile
import django.contrib.staticfiles
from django.forms import forms 
from django.views.generic import TemplateView
from .forms import FillProfileForms
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User
from django.shortcuts import get_object_or_404
from pages.forms import ChangeProfileForms

class HomePageView(TemplateView):
    template_name = "home.html"
@login_required
def Fillprofileview(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        myuser = get_object_or_404(User, pk=request.user.id)
        form = FillProfileForms(request.POST)
        
        # Check if the form is valid:
        if form.is_valid():
            myuser.company_name = form.cleaned_data['company_name']
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
            print(myuser.profile_set)
            print(myuser.username)
            return HttpResponseRedirect('/showprofile/')
    # If this is a GET (or any other method) create the default form.
    else:
        form = FillProfileForms()

    context = {
        'form': form,
    }

    return render(request,'fillprofile.html', {
        'form': form,
    })
@login_required
def Changeprofileview(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        myuser = get_object_or_404(User, pk=request.user.id)
        print("ddddddddddddddddddddddddddddddddd")
        form = ChangeProfileForms(request.POST)
        
        # Check if the form is valid:
        if form.is_valid():
            myuser.company_name = form.cleaned_data['company_name']
            myuser.organic_numb_certification = form.cleaned_data['organic_numb_certification']
            myuser.CNPJ = form.cleaned_data['CNPJ']
            myuser.profile_set = True
            myuser.city = form.cleaned_data['city']
            myuser.first_name = form.cleaned_data['first_name']
            myuser.last_name = form.cleaned_data['last_name']
            myuser.state = form.cleaned_data['state']
            myuser.country = form.cleaned_data['country']
            print(myuser.birthday)
            myuser.birthday = form.cleaned_data['birthday']
            print(myuser.birthday)
            print("OOOOOOOOOOOOOOOOOi")
            myuser.save()
            print(myuser.profile_set)
            print(myuser.birthday)
            print(myuser.username)
            return HttpResponseRedirect('/showprofile/')
    # If this is a GET (or any other method) create the default form.
    else:
        form = ChangeProfileForms()

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

def EndUserView(request):
    user = User
    return render(request,"enduser.html",{'User': User,})  
