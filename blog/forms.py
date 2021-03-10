from django import forms
from django.contrib.auth import get_user_model
from .models import Blog_post, Blog_comments,Query
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class QueryForm(forms.ModelForm):
    class Meta():
        model = Query
        fields = "__all__"
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'Email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'Title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
            'Content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Content'}),
        }



class PostForm(forms.ModelForm):
    class Meta():
        model = Blog_post
        fields = ("title","text",)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control','placeholder':'Content'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Blog_comments
        fields = ('text',)

        widgets = {
            
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

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
        
    
