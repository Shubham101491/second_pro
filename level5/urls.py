from collections import namedtuple
from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'level5'

urlpatterns = [
    path('',views.index,name='index'),
    # path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('user_login/',views.user_login,name='user_login')
]