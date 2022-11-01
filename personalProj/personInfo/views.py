from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def homepage (requste:HttpRequest):
    name = "ASRAR ALRASHED"

    return render(requste,'personInfo/base.html', {"name":name})

