
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest

def index(request : HttpRequest):
    context = {
        'R' : []
    }
    return render(request , 'Web/index.html' , context)

