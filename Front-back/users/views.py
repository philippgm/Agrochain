from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from forms import ProfileForms
# Create your views here.

def FillprofileView(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Fillprofile(request.POST)

        # Check if the form is valid:

    # If this is a GET (or any other method) create the default form.
    else:
        form = Fillprofile(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
    }

    return render(request, 'tamplates/fillprofile.html', context)