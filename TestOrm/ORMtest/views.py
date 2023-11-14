from django.shortcuts import render as RD

from django.http import HttpResponse as HR

def hola(requests):
    return RD(requests,'hola.html')

# Create your views here.
