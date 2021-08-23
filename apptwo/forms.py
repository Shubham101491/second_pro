from django import forms

# Validator for form
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcather = forms.CharField(required=False,widget=forms.HiddenInput,
                            validators=[validators.MaxLengthValidator(0)])