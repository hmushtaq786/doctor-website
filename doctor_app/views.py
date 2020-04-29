from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Service, FAQ, ClientTestimonial, Blog
import datetime

# Create your views here.


def index(request):
    data = {'page': 'Home', 'home': True}
    return render(request, 'index.html', context=data)


def about(request):
    testimonials_list = ClientTestimonial.objects.order_by('client_name')
    data = {'page': 'About', 'about': True, 'testimonials': testimonials_list}
    return render(request, 'about.html', context=data)


def blog(request):
    blogs_list = Blog.objects.order_by('-posted_date')
    data = {'page': 'Blog', 'blog': True, 'blogs': blogs_list}
    return render(request, 'blog.html', context=data)


def services(request):
    services_list = Service.objects.order_by('service_heading')
    faqs_list = FAQ.objects.order_by('question')
    data = {'page': 'Services', 'services': True,
            'services': services_list, 'faqs': faqs_list}
    return render(request, 'services.html', context=data)


def contact(request):
    data = {'page': 'Contact', 'contact': True}
    return render(request, 'contact.html', context=data)
