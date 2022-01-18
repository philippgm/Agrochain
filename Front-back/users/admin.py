from django.contrib import admin
from django.contrib.auth import admin as auth_admin, forms
from .models import User
from .forms import UserChangeForm,UserCreationForm 

# admin.site.register(User, auth_admin.UserAdmin)
# Register your models here.

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User