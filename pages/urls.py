from django.urls import path,include
from django.contrib.auth.models import User
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from product.views import CadastrarProdutoView

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/profile/",views.ProfileView, name ="profile"),
    path("accounts/",views.HomePageView.as_view(), name="home"),
    # path("fillprofile/",views.Fillprofileview, name="fillprofile"),
    path("changeprofile/",views.Changeprofileview, name="changeprofile"),
    path("showprofile/",views.ProfileView, name="showprofile"),
    # path("accounts/cadastraproduto/",views.CadastrarProdutoView,name="cadastrarproduto" ),  
    path("main/",views.how, name="main"),
    path("creator/",views.CreatorView, name="creator"),
    path("enduser/",views.EndUserView, name="enduser"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
