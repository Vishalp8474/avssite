from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from avswep.models import Registeration

# Create your views here.


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def aboutus(request):
  template = loader.get_template('aboutus.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())

def course(request):
  template = loader.get_template('course.html')
  return HttpResponse(template.render())


def user(request):
   template = loader.get_template('user.html')
   return HttpResponse(template.render())
  

def contact(request):
   template = loader.get_template('contact.html')
   return HttpResponse(template.render())

def registerations(request):
    if request.method=="POST":
       print("ghghg")
       certificate=request.POST.get('certificate')
       studentname=request.POST.get('studentname')
       farthername=request.POST.get('farthername')
       mothername=request.POST.get('mothername')
       date=request.POST.get('date')
       caursename=request.POST.get('caursenamete')
       duration=request.POST.get('duration')
       caursestatus=request.POST.get('caursestatus')
       
     
       mydata=Registeration(certificate=certificate,studentname=studentname, farthername=farthername, mothername=mothername, date=date, caursename=caursename, duration=duration, caursestatus=caursestatus)
       mydata.save()
       print(mydata)
    return render(request, "Registeration.html")
    
# ----------------Create user Login -----------------------
 


def Register(request):
    if request.method =="POST":
      first_name=request.POST.get("first_name")
      last_name=request.POST.get("last_name")
      username=request.POST.get("username")
      password=request.POST.get("password")

      user = User.objects.filter(username=username)
      if user.exists():
       messages.warning(request, "User name already taken")
       return redirect('/register/')


      user=User.objects.create(
      first_name=first_name,
      last_name=last_name,
      username=username,
        )

      user.set_password(password) # for send  incript password
      user.save()
      messages.warning(request, "Account crated successfully")
      return redirect('/register/')
    return render(request, "user_templates/register.html")

# login page----------------

def log (request):
    
    if request.method =="POST":
        
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists:
            messages.warning(request, "Enter correct username")
            return redirect('/login/')
        
        
        user=authenticate(username=username,password=password)
        if user is None:
             messages.warning(request, "Enter correct username")
             return redirect('/login/')
        else:
             
             login(request,user) 
             return redirect('/home/')
    return render(request, "user_templates/login.html")



