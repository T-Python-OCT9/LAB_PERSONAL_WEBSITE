from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    #return HttpResponse ('hello Ahmad')
    return render(request, 'Website/index.html',{})

def about (request):
   # return HttpResponse ('wellcome back')
    return render(request, 'Website/about.html',{})

