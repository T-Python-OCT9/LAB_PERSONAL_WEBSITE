from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def Abuot_me(request: HttpRequest):
    my_self = ['']
    context = {'myself' : my_self}
    return render(request, 'myWebsite/about.html', context)

def contact(request: HttpRequest):
    concat_co = ['']
    context = {'con' : concat_co}
    return render(request, 'myWebsite/contact.html', context)

