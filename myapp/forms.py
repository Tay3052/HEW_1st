from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class userForm(forms.ModelForm):
    class Meta:
        model = userTable
        fields = ("id", "password", "password_check", "mail")

class chatForm(forms.ModelForm):
    class Meta:
        model = chatTable
        fields = ("userName", "title", "genre","text", "img")

class loginForm(forms.ModelForm):
    class Meta:
        model = loginTable
        fields = ("__all__")

class LoginForm1(AuthenticationForm):
    pass