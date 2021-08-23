from typing import FrozenSet
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, redirect, HttpResponse
from mfapp.models import User
from mfapp.forms import User_Form
from protwo import settings

def index(request):
    form = User_Form()
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            return redirect('index/')
    return render(request, 'mfapp/user.html', {"BASE_URL":settings.BASE_URL,'form': form})


def home(request):
    return HttpResponse('Form Submitted!',{"BASE_URL":settings.BASE_URL})

# Long Style
# def new(request):
#     data = {}
#     data ['text'] = 'hello world!'
#     data ['num'] = 100
#     data ['BASE_URL'] = settings.BASE_URL
#     return render(request,'mfapp/new.html',data)

# Short Style
def new(request):
    context = {'text':'hello world!','num':100,"BASE_URL":settings.BASE_URL}
    return render(request,'mfapp/new.html',context)