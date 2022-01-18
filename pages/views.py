import django.contrib.staticfiles 
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class FillprofileView(TemplateView):
    template_name = "profile.html"

class ShowprofileView(TemplateView):
    template_name = "showprofile.html"

