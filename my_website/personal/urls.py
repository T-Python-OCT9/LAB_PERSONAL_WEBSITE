from django.urls import path
from . import views

app_name = "my_website"

urlpatterns = [

path("home/", views.myhomepage, name = "home"),
path("aboutme/" , views.aboutme, name = "about"),
]