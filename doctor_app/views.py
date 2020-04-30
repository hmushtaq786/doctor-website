from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Service, FAQ, ClientTestimonial, Blog
import datetime

# Create your views here.


def index(request):
    appointment_form = forms.AppointmentForm()
    subscriber_form = forms.SubscriberForm()

    a_html = None
    s_html = None

    if request.method == 'POST':
        appointment_form = forms.AppointmentForm(request.POST)
        subscriber_form = forms.SubscriberForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save(commit=True)
            request.method = "GET2"
            return index(request)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return index(request)

    if request.method == 'GET2':
        a_html = """
            <div id="appoint_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="appoint_close" class="close">&times;</span>
                    <p>Appointment scheduled for given time.</p>
                </div>
            </div>
        """
    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    data = {'page': 'Home', 'home': True, 'appointment_form': appointment_form,
            'subscriber_form': subscriber_form, 'a_html': a_html, 's_html': s_html}
    return render(request, 'index.html', context=data)


def about(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return about(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    testimonials_list = ClientTestimonial.objects.order_by('client_name')
    data = {'page': 'About', 'about': True,
            'testimonials': testimonials_list, 'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'about.html', context=data)


def blog(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return blog(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    blogs_list = Blog.objects.order_by('-posted_date')
    data = {'page': 'Blog', 'blog': True, 'blogs': blogs_list,
            'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'blog.html', context=data)


def services(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return services(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    services_list = Service.objects.order_by('service_heading')
    faqs_list = FAQ.objects.order_by('question')
    data = {'page': 'Services', 'services': True,
            'services': services_list, 'faqs': faqs_list,  'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'services.html', context=data)


def contact(request):
    appointment_form = forms.AppointmentForm()
    subscriber_form = forms.SubscriberForm()

    a_html = None
    s_html = None

    if request.method == 'POST':
        appointment_form = forms.AppointmentForm(request.POST)
        subscriber_form = forms.SubscriberForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save(commit=True)
            request.method = "GET2"
            return contact(request)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return contact(request)

    if request.method == 'GET2':
        a_html = """
            <div id="appoint_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="appoint_close" class="close">&times;</span>
                    <p>Appointment scheduled for given time.</p>
                </div>
            </div>
        """
    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    data = {'page': 'Contact', 'contact': True,  'appointment_form': appointment_form,
            'subscriber_form': subscriber_form, 'a_html': a_html, 's_html': s_html}
    return render(request, 'contact.html', context=data)
