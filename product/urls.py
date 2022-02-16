from django.urls import path,include
from django.contrib.auth.models import User
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CadastrarProdutoView,ShowProductInfoView

app_name = "product"

urlpatterns = [
    
    path("cadastrarproduto/",views.CadastrarProdutoView,name="cadastrarproduto" ),
    path("pesquisarproduto/",views.PesquisarProdutoView,name="pesquisarproduto" ), 
    path("showproductinfo/<int:id>/", views.ShowProductInfoView, name="showproductinfo"),
    path("checkin/", views.CheckinProduct, name="checkin"),
    path("checkinproduct/<int:id>/", views.CheckinProductView, name="checkinproduct"),
    path("checkout/", views.CheckoutProduct, name="checkout"),
    path("checkoutproduct/<int:id>/", views.CheckoutProductView, name="checkoutproduct"),
    path("comprarproduto/<int:id>/",views.ComprarProdutoView,name="showcomprarproduto" ),
    path("comprarproduto/",views.ComprarProduto,name="comprarproduto" ),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
