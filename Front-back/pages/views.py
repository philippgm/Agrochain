import django.contrib.staticfiles 
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class FillprofileView(TemplateView):
    template_name = "fillprofile.html"

class ShowprofileView(TemplateView):
    template_name = "showprofile.html"

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
