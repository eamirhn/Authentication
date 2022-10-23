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
    path('researcher/comments/<int:data_id>/',commentView,name='comments'),
    path('researcher/comments/delete/<int:id>/<int:data_id>/',deleteCommentView,name='delete')
]
