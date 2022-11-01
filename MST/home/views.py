from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def home(request : HttpRequest):
    x = {'name': 'ahmed','file' : 353524000256}

    return render(request,'index.html',x)

def me(request : HttpRequest):

    return render(request,'me.html')
    
