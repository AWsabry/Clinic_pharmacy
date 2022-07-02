import imp
from django.urls import path
from doctor import views


app_name = 'doctor'

urlpatterns = [

    path('get_medcine/', view=views.get_medcine, name='get_medcine'),
    path('get_roshetta/', view=views.get_roshetta, name='get_roshetta'),




]
