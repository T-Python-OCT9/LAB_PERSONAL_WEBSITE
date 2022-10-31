from django.urls import path
from . import views

app_name = "MyWebSite"

urlpatterns = [
    path("AboutMe/", views.about_me,  name="About Me"),
    path("Education/", views.education, name="Education"),
    path("TrainigPrograms/", views.trainig_programs , name=" Trainig Programs"),
    path("Skills/", views.skills ,  name="Skills"),
]