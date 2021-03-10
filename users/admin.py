from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserAdmin(admin.ModelAdmin):
    fields = ('password','username', 'email','is_superuser','is_active','name','first_name','last_name','last_login','date_joined','phone','linkedin','twitter','Instagram') # Enter full list of fields here

# admin.site.unregister(UserAdmin)
admin.site.register(User,UserAdmin)
