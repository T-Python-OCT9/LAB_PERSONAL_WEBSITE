from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def base(request : HttpRequest):
  return render(request, 'base.html')
