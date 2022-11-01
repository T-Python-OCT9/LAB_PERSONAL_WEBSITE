from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




def home_Page (request: HttpRequest) :
    return render (request , "About/base.html")

def esport_Page (request: HttpRequest) :
    return render (request , "About/Aboutme.html")    
# Create your views here.
def video_Page (request: HttpRequest) :
    return render (request , "About/clips.html")