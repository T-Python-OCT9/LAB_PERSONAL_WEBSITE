from django.urls import path
from.import views

app_name="AlaaAlfraih"

urlpatterns = [
    path('home/',views.basic,name="Alaa"),
    path('Web',views.alaaWeb,name="AlaaWeb"),
    path('con',views.con,name="con"),
    path('project',views.project,name="project")
   


]