from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def about_me(request:HttpRequest):

    text1 = "Athari Alharbi: "    
    return render(request, 'MyWebSite/index.html', {"text" : text1})
    


def education(request:HttpRequest):

    text_education = ""

    text_certificates = ""

    return HttpResponse(text_education,text_certificates) 


def trainig_programs(request:HttpRequest):

    train1  = "Acquired training programs: " 
   

    return render(request, 'MyWebSite/train.html', {"train" : train1 }) 


def skills(request:HttpRequest): 

    text2 = " "

    return render(request, 'MyWebSite/skill.html', {"skill" : text2 }) 
