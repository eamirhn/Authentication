from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signUpView, name='signUp'),
    path('login/', loginView, name='login'),
    path('', homeView, name='home'),
    path('logout/', logOutView, name='logOut'),
    path('parkinson/',parkinsonView,name='parkinson'),
    path('patient/',patientView,name='patient'),
    path('researcher/',researcherView,name='researcher'),
    path('physician/',physicianView,name='physician'),
]
