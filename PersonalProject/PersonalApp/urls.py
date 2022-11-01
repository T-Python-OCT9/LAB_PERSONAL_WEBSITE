from django.urls import path     
from . import views

app_name = 'PersonalApp'
urlpatterns = [
    path('about/', views.aboutMe, name="about"),
    path('home/', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('contact/', views.contact, name="contact"),




]