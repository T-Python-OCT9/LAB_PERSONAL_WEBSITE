from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def MyHome(request: HttpRequest):
    context = {
        "title" : "أهـــلاَ", 
    }
    return render(request, "MyHome/index.html", context)
def aboutme(request:HttpRequest):
    context = {
        
        
    }
    return render(request,"MyHome/index.html",context)

def hobbies(request:HttpRequest):
    context = {
        
    }
    return render(request,"MyHome/index.html",context)
def intrested (request:HttpRequest):
    context = {
        
    }
    return render(request,"MyHome/index.html",context)
def contact(request:HttpRequest):
    context = {
      
    }
    return render(request,"MyHome/index.html",context)