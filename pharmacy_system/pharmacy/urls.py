import imp
from django.urls import path
from pharmacy import views


app_name = 'pharmacy'


urlpatterns = [
    path('', view=views.index, name='index'),
    path('get_roshetta/', view=views.get_roshetta, name='get_roshetta'),

]
