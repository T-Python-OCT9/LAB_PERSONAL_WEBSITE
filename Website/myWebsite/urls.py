from django.urls import path
from . import views

app_name = "myWebsite"

urlpatterns = [

    path("about/", views.Abuot_me ,name = "about"),
    path("contact/", views.contact ,name = "contact")
]