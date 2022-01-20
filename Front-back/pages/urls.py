
from django.contrib.auth.models import User
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    # path("accounts/profile/",views.ProfileView.as_view(), name ="profile"),
    path("accounts/",views.HomePageView.as_view(), name="home"),
    path("showprofile/",views.ShowprofileView.as_view(), name="showprofile"),
    path("fillprofile/",views.FillprofileView.as_view(), name="fillprofile"),
    path("produtor/",views.ProdutorView.as_view(), name="produtor"),
    path("transportador/",views.TransportadorView.as_view(), name="transportador"),
    path("processador/",views.ProcessadorView.as_view(), name="processador"),
    path("distribuidor/",views.DistribuidorView.as_view(), name="distribuidor"),
    path("consumidor/",views.ConsumidorView.as_view(), name="consumidor"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
