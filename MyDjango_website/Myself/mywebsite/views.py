from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request:HttpRequest):
    return render(request, 'mywebsite/base.html')


def favsports(request:HttpRequest):
    context = {"sports": ["football", "Swimming", "Coding", "Camping"]
    }
    return render(request, 'mywebsite/favsport.html', context)

def information(request:HttpRequest):
    return render(request, 'mywebsite/info.html')
