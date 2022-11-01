from django.urls import path
from . import views

app_name = "personInfo"

urlpatterns = [
    path("info/",views.homepage , name = "infoPage"),
]