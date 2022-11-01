from django.urls import path 
from . import views

app_name = "my_blog"

urlpatterns = [
path("base/", views.base, name="home")
]
