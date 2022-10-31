from django.urls import path
from .views import homePage

app_name = 'website'

urlpatterns = [
    path('', homePage, name='home')
]