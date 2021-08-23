from django import forms
from django.shortcuts import render
from django.http import HttpResponse

# Use Model
from apptwo import models
from apptwo.models import Topic,AccessRecord,Webpage

# Use Form
from apptwo.forms import FormName

def index(request):
    return HttpResponse('<em> My Second App <em>')

def index2(request):
    data = {'abc':'alphabat'}
    return render(request,'apptwo/index.html',context=data)

def list(request):
    webpg = Webpage.objects.order_by('name')
    date_dict = {'webpg':webpg}
    return render(request,'apptwo/list.html',date_dict)

def form(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)
        
        if form.is_valid():
            # Do Something Code
            print("Validation Success")
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])

    return render(request,'apptwo/form.html',{'form':form})