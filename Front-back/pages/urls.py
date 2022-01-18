
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
    path("fillprofile/",views.FillprofileView, name="fillprofile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)