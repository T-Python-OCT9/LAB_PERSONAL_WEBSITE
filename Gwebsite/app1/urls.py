
from django import views

from django.urls import path
from . import views
app_name='app1'

urlpatterns=[
path('home/', views.home , name ="home"),
path('projects/',views.projects , name="projects"),
path('/courses',views.courses , name="courses"),
path('contact/',views.contact , name="contact")
]