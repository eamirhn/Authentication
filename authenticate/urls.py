from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signUpView, name='signUp'),
    path('login/', loginView, name='login'),
    path('', homeView, name='home'),
    path('logout/', logOutView, name='logOut'),
    path('parkinson/',parkinsonView,name='parkinson')
]
