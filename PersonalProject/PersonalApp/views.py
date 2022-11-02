
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request:HttpRequest):

    return render(request,'PersonalApp/home.html')

def resume(request:HttpRequest):

    return render(request,'PersonalApp/Resume.html' )

def work(request:HttpRequest):

    return render(request,'PersonalApp/work.html' )

def contact(request:HttpRequest):

    return render(request,'PersonalApp/contact.html')
