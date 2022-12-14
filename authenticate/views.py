from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import commentsForm


def signUpView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print('Post is okay')
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} has been created!')
            login(request, User.objects.get(username=user))
            print('created')
            return redirect('/')

        else:
            print("didn't create user")
            arg = {'form': form}
            return render(request, 'authenticate/signUp.html', arg)

    else:

        form = CreateUserForm()
    arg = {'form': form}
    return render(request, 'authenticate/signUp.html', arg)


def homeView(request):
    return render(request, 'homePage.html')


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome {user}')
            return redirect('/')
        else:
            arg = {'form': form}
            return render(request, 'authenticate/login.html', arg)
    else:
        form = AuthenticationForm()
    arg = {'form': form}
    return render(request, 'authenticate/login.html', arg)


def logOutView(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Goodbay!')
        return redirect('/login/')


def parkinsonView(request):
    return render(request, 'authenticate/data_parkinson.html')

def patientView(request):
    return render(request, 'authenticate/patient.html')

def physicianView(request):
    context = User.objects.filter(Role_IDrole=1)
    arg = {'users':context,
    'note':Note.objects.all(),
    'tests':Test.objects.all(),
    'organization':Organization.objects.all(),
    'therapy_list':Therapy_List.objects.all(),
    'test_session':Test_Session.objects.all()}
    return render(request, 'authenticate/physician.html',arg)
    
def researcherView(request):
    context = User.objects.filter(Role_IDrole=1)
    arg = {'users':context,
    'note':Note.objects.all(),
    'tests':Test.objects.all(),
    'organization':Organization.objects.all(),
    'therapy_list':Therapy_List.objects.all(),
    'test_session':Test_Session.objects.all()}
    return render(request, 'authenticate/researcher.html',arg)



def commentView(request,data_id):
    form = commentsForm()
    arg = {
        'id':data_id,
        'form':form,
        'comments': reversed(Comments.objects.filter(data_id=data_id))

    }
    if request.method == 'POST':
        form = commentsForm(request.POST)
        comment = form.data['comment']
        print(request.user.username)
        object = Comments.objects.create(user=request.user.username,comment=comment,data_id=data_id)
        object.save()
        return redirect('/researcher/comments/'+str(data_id)+'/')
    else:
        return render(request,'authenticate/comments.html',arg)


def deleteCommentView(request,id,data_id): 
    Comments.objects.get(id=id).delete()
    return redirect('/researcher/comments/'+str(data_id)+'/')   


