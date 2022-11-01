from django.urls import path
from . import views

app_name = "SamaaSite"

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("myworks/", views.myworks, name = "myworks"),
    path("workwithme/", views.workwithme, name = "workwithme"),
    path("about/", views.about, name = "about"),
]
