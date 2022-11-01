from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def home(request):
    return HttpResponse("Hello world!")

# Create your views here.

def homeView(request: HttpRequest):
    return render(request, 'website/index.html')


def about(request: HttpRequest):
    return render(request, 'website/about.html')

class main():
    pass

def programming(request: HttpRequest):
    return render(request, 'website/index.html')

def courses(request: HttpRequest):
    return render(request, 'website/index.html')