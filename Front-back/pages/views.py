import django.contrib.staticfiles 
from django.views.generic import TemplateView
from .forms import FillProfileForms
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


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

class ShowprofileView(TemplateView):
    template_name = "showprofile.html"

