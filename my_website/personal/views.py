from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def myhomepage(request : HttpRequest):
    return render (request , "personal/base.html")

def  aboutme(request : HttpRequest):
    return render (request , "personal/about.html")


