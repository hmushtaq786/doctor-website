from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.


def index(request):
    data = {'page': 'Home', 'home': True}
    return render(request, 'index.html', context=data)


def about(request):
    data = {'page': 'About', 'about': True}
    return render(request, 'about.html', context=data)


def blog(request):
    data = {'page': 'Blog', 'blog': True}
    return render(request, 'blog.html', context=data)


def services(request):
    data = {'page': 'Services', 'services': True}
    return render(request, 'services.html', context=data)


def contact(request):
    data = {'page': 'Contact', 'contact': True}
    return render(request, 'contact.html', context=data)
