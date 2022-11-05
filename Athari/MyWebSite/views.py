from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def about_me(request:HttpRequest):

    text1 = "Athari Alharbi: "    
    return render(request, 'MyWebSite/index.html', {"text" : text1})
    


def education(request:HttpRequest):

    

    return render(request, 'MyWebSite/edu.html', ) 


def trainig_programs(request:HttpRequest):

    train1  = "Acquired training programs: " 
   

    return render(request, 'MyWebSite/train.html', {"train" : train1 }) 


def skills(request:HttpRequest): 

    text2 = "skills: "

    return render(request, 'MyWebSite/skill.html', {"skill" : text2 }) 

def MyProject(request:HttpRequest): 

    project = "Graduation Project:-"

    return render(request, 'MyWebSite/project.html',{"project" : project})     
