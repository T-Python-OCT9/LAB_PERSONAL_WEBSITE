from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def aboutMe(request:HttpRequest):
    context = {
        'name': "Roaa Albishri"
    }
    return render(request,'PersonalApp/base.html' , context)

def home(request:HttpRequest):

    return render(request,'PersonalApp/Home.html')

def resume(request:HttpRequest):

    return render(request,'PersonalApp/resume.html' )

def work(request:HttpRequest):

    return render(request,'PersonalApp/work.html' )

def contact(request:HttpRequest):

    return render(request,'PersonalApp/contact.html')
