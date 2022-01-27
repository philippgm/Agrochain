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

class HomePageView(TemplateView):
    template_name = "home.html"

def Fillprofileview(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        myuser = get_object_or_404(User, pk=request.user.id)
        form = FillProfileForms(request.POST)
        
        # Check if the form is valid:
        if form.is_valid():
            myuser.company_name = form.cleaned_data['company_name']
            myuser.organic_numb_certification = form.cleaned_data['organic_numb_certification']
            myuser.profile_set = True
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
def ProfileView(request):
    user = User
    return render(request,"account/profile.html",{'User': User,})

class ProdutorView(TemplateView):
    template_name = "produtor.html"

class TransportadorView(TemplateView):
    template_name = "transportador.html"

class ProcessadorView(TemplateView):
    template_name = "processador.html"

class DistribuidorView(TemplateView):
    template_name = "distribuidor.html"

class ConsumidorView(TemplateView):
    template_name = "consumidor.html"
