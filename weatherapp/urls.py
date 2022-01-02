from django.urls import path
from . import views

app_name = 'weatherapp'

urlpatterns = [
     path('', views.description),
     path('the_weather', views.the_weather),
]