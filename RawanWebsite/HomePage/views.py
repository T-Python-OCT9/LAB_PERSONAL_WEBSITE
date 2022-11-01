from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def Home(request : HttpRequest):

    return render(request  , 'home.html' )


def Education(request : HttpRequest):
 
    return render(request ,'Education.html' )

def About(request : HttpRequest):
    
    return render(request ,'About.html' )


def Contact(request : HttpRequest):

    return render(request ,'contact.html' )
