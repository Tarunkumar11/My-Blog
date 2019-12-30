from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Comment,Query
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class QueryForm(forms.ModelForm):
    class Meta():
        model = Query
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("title","text",)


        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'title'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        fields = ("first_name","last_name","username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"
        self.fields["last_name"].label = "Sirname"
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
