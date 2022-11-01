from django.urls import path
from . import views

app_name = "HomePage"
urlpatterns = [

    path('home/' , views.Home , name='Home'),
    path('contact/' , views.Contact , name='Contact'),
    path('Education/' , views.Education, name='Education'),
    path('About/' , views.About, name='About')

]