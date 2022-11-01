from django.urls import path

from . import views



app_name = 'About_me'


urlpatterns = [
 path ('home/',views.home_Page,name='HomePage'),
 path('esport/',views.esport_Page,name='esport'),
 path('clips/',views.video_Page, name = 'Clips')
]