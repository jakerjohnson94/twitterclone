from django import forms
from .models import TwitterUser
from django.contrib.auth.models import User


class TwitterUserSignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    handle = forms.CharField(max_length=16)

