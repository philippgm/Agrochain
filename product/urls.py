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


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
