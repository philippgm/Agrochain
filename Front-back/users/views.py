from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ProfileForms
# Create your views here.
def FillprofileView(request):
    submitted = False
    if request.method == 'POST':
        form = ProfileForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fillprofile/?submitted=True')
    else:
        form = ProfileForms()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 
        'fillprofile.html', 
        {'form': form, 'submitted': submitted}
        )