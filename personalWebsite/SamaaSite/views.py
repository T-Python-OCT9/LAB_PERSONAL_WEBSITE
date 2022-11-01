from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date

# Create your views here.
def home(request : HttpRequest):

 return render(request, 'SamaaSite/home.html')

def myworks(request : HttpRequest):

 return render(request, 'SamaaSite/myworks.html')

def about(request : HttpRequest):

 return render(request, 'SamaaSite/about.html')

def workwithme(request : HttpRequest):

 return render(request, 'SamaaSite/workwithme.html')