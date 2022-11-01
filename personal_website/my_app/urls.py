from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "my_app"


urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),

    # path('today/', views.today_date, name="today_date"),
    # path('random/password', views.randomly_password, name="randomly_password"),
    #  path('favs/games/', views.favorite_games, name="favorite_games"),
]
