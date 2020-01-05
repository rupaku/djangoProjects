from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse('Hola means hello in english')

# Create your views here.
