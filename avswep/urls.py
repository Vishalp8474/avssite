from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('gallery/', views.gallery, name='gallery'),
    path('course/', views.course, name='course'),
    path('Registeration/', views.registerations, name='registerations'),
    path('register/', views.Register, name='register'),
    path('login/', views.log, name='login'),
    path('contact/', views.contact, name='contact'),
    
]