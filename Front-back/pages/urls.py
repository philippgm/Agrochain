
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
    path("accounts/profile/",views.ProfileView, name="profile"),
    path("fillprofile/",views.Fillprofileview, name="fillprofile"),
    path("showprofile/",views.ProfileView, name="showprofile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
