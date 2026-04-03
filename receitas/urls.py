from django.http import HttpResponse
from django.urls import path
from receitas.views import home,Sobre


urlpatterns = [
    path('',home ),
    path('Sobre/', Sobre),
    
]