from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('colleage\\',views.colleage, name = 'colleage'),
    path('x\\',views.connect, name = 'connect'),
]