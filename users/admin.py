from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django import forms
# class UserAdmin(admin.ModelAdmin):
#     fields = ('password','username', 'email','is_superuser','is_active','name','first_name','last_name','last_login','date_joined','phone','linkedin','twitter','Instagram') # Enter full list of fields here

admin.site.register(User,UserAdmin)
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    error_messages = UserCreationForm.error_messages.update({'email_error': 'Email already exist'})
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['email_error'])


