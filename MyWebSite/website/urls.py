from django.urls import path
from .views import homePage, aboutPage, contactPage

app_name = 'website'

urlpatterns = [
    path('', homePage, name='home'),
    path('about/', aboutPage, name='about'),
    path('contact/', contactPage, name='contact'),
]