
from django.http import HttpRequest
from django.shortcuts import render
# HttpResponse
# Create your views here.

# This should display the date of today .


def home(request: HttpRequest):

    return render(request, "my_app/home.html")


def projects(request: HttpRequest):

    return render(request, "my_app/projects.html")


def contact(request: HttpRequest):

    return render(request, "my_app/contact.html")


def about(request: HttpRequest):

    return render(request, "my_app/about.html")
