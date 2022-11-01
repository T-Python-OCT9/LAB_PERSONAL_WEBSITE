import imp
from django.shortcuts import render
from django.http import HttpRequest



def basic (request:HttpRequest):
    return render(request,'AlaaAlfraih/basic.html')


def alaaWeb (request:HttpRequest):
    return render(request,'AlaaAlfraih/AlaaWeb.html')


def project (request:HttpRequest):
    return render(request,'AlaaAlfraih/con.html')

def con (request:HttpRequest):
    return render(request,'AlaaAlfraih/con.html')







# Create your views here.
