from django.urls import path
from . import views

app_name = "MyHome"

urlpatterns = [
    path("home/", views.MyHome, name = "MyHome"),
    path("aboutme/",views.aboutme,name="aboutme"),
    path("hobbies/",views.aboutme,name="hobbies"),
    path("intrested/",views.aboutme,name="intrested"),
    path("contact/",views.aboutme,name="contact"),
]