from django import forms
from django.db import models
from django.forms import fields
from level5.models import userinfo,User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

# Note = use username and email to set length, password use for hidden type password
# othervies we use only password

    class Meta():
        model = User
        fields = ['username','email','password']

class UserinfoForm(forms.ModelForm):
    class Meta():
        model = userinfo
        exclude = ['user',]

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())