import django.contrib.staticfiles 
from django.views.generic import TemplateView
from .forms import FillProfileForms
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User

class HomePageView(TemplateView):
    template_name = "home.html"

def Fillprofileview(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = FillProfileForms(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            
            return HttpResponseRedirect('/thanks/')
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
