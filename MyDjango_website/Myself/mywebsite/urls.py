from django.urls import path
from . import views


app_name = "MyWebsite"
urlpatterns = [
    path('', views.home, name = "Home"),
    path('favsports', views.favsports, name="FavSports"),
    path('info/', views.information, name="Info")
]