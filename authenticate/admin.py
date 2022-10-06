from urllib.parse import uses_relative
from django.contrib import admin
from .models import *

#admin.site.register(Role, Medicine,Therapy_List,Therapy,Test,Test_Session,Note,Organization)
models_register = [Role, Medicine,Therapy_List,Therapy,Test,Test_Session,Note,Organization,User]
admin.site.register(models_register)