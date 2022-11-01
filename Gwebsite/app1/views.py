from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request: HttpRequest):

    return render(request, "app1/aboutme.html")

def projects(request: HttpRequest):
    return render(request, "app1/projects.html")


def courses(request: HttpRequest):
     return render(request, "app1/courses.html")

def contact(request: HttpRequest):
     return render(request, "app1/contact.html")