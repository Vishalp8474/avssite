from django.contrib import admin
from .models import Registeration
from avswep import models


# Register your models here.

class  Registerationadmin(admin.ModelAdmin):
  list_display=('certificate', 'studentname', 'farthername', 'mothername', 'caursename', 'caursestatus','duration' , 'date', 'photo')
  
admin.site.register(Registeration,  Registerationadmin)
