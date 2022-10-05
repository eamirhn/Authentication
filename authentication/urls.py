
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('', include('authenticate.urls')),
    path('accounts/',include('allauth.urls'))
]
