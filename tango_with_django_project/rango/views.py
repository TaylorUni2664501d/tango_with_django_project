from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>about page</a>")


def about(request):
    return HttpResponse("Rango says this here is the about page. <a href='/rango/'>index page</a>")
