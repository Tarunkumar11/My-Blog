from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        fields = ("first_name","username", "email", "password1", "password2")
        model = get_user_model()
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["first_name"].label = "Name"
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        
    
