from django import forms
from mfapp.models import User

class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
