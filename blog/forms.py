from django import forms
from django.contrib.auth.models import User
from .models import Post, MyUser

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class SingInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')