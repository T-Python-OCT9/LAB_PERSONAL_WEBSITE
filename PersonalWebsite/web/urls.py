from django.urls import path
from django.http import HttpResponse, HttpRequest
from . import views


app_name = "web"


urlpatterns = [
    
    path("", views.home_page, name="home_page"),
    path("home/", views.home_page, name="home_page"),
    path("about/", views.about_me, name="about_me"),
    path("contact/", views.contact_me, name="contact_me"),


]