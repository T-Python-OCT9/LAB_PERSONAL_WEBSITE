from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def home(request : HttpRequest):
    return render(request,"personal/home.html")

def about(request : HttpRequest):
    return render(request,"personal/about.html")

def my_work(request : HttpRequest):
    return render(request,"personal/my_work.html")

def contact(request : HttpRequest):
    return render(request,"personal/contact.html")