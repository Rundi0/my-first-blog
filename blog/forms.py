from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms.widgets import PasswordInput
from .models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class SingInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': PasswordInput()
        }

class RegistrationForm(forms.ModelForm):
    repeat_password = CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        widgets = {
            'password': PasswordInput()
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text' : (''),
        }