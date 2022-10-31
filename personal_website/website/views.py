from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest): 
    context = {'msg':'Welcom'}
    return render(request, "website/base.html", context)

def colleage(request: HttpRequest): 

    return render(request, "website/colleage.html")