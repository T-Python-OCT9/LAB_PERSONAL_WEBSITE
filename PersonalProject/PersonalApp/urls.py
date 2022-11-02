from django.urls import path     
from . import views

app_name = 'PersonalApp'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('work/', views.work, name="work"),
    path('contact/', views.contact, name="contact"),




]