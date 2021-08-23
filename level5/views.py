from django.forms.fields import DateField
from django.http.response import HttpResponse
from level5.models import userinfo
from django.shortcuts import redirect, render
from protwo import settings
from level5.forms import UserForm,UserinfoForm,UserLoginForm

# Extra Copy Fields
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login

def index(request):
    registered = False   # for loop {% if registered in html %}
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = UserinfoForm(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            # Now Link both model
            profile.user = user

            # Here, profile object represents the profileform.
            # If user upload the picture successfully, then the system will check the picture folder
            # and capture the path image path and save it to the picture field.
            if 'picture' in request.FILES:
                print('found it')
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            return redirect('user_login/')
    else:
        userform = UserForm()
        profileform = UserinfoForm()
        
    data_dict = {'registered':registered,'userform':userform,'profileform':profileform,"BASE_URL":settings.BASE_URL}
    return render(request,'level5/index.html',data_dict)

# def login(request):
#     form = UserLoginForm()
#     data_dict = {'form':form,"BASE_URL":settings.BASE_URL}
#     return render(request,'level5/login.html',data_dict)
    
def home(request):
    return render(request,'level5/home.html',{"BASE_URL":settings.BASE_URL})

# Copy LOgin
def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        #Nothing has been provided for username or password.
        return render(request, 'level5/login2.html', {})