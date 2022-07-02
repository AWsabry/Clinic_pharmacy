import imp
from django.urls import path
from django.contrib.auth import views
from patient.views import register,login,index,logOut,appointment


app_name = 'patient'

urlpatterns = [
    path('', view=index, name='index'),
    path('register', view=register, name='register'),
    path('login', view=login, name='login'),
    path('logOut', view=logOut, name='logOut'),
    path('appointment', view=appointment, name='appointment'),


]
