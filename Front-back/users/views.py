from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from forms import FillProfileForms
# Create your views here.

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

    return render(request, 'templates/fillprofile.html', context)
