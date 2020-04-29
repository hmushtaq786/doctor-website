from django.db import models
from django.conf import settings
from django.apps import apps

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Email', blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ClientTestimonial(models.Model):
    client_name = models.CharField(
        max_length=50, verbose_name='Client name', blank=True)
    client_testimonial = models.TextField(
        verbose_name='Client testimonial', blank=True)
    client_picture = models.ImageField(
        verbose_name='Client picture', upload_to='clients/', blank=True)

    def __str__(self):
        return self.client_name


class FAQ(models.Model):
    question = models.CharField(
        max_length=100, verbose_name='Question', blank=True)
    answer = models.TextField(verbose_name='Answer', blank=True)

    def __str__(self):
        return self.question


class Service(models.Model):
    service_heading = models.CharField(
        max_length=40, verbose_name='Service heading', blank=True)
    service_description = models.TextField(
        verbose_name='Service description', blank=True)

    def __str__(self):
        return self.service_heading


class Blog(models.Model):
    blog_title = models.CharField(
        max_length=50, verbose_name='Blog title', blank=True)
    blog_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name='Blog author')
    blog_topic = models.CharField(
        max_length=20, verbose_name='Blog topic', blank=True)
    blog_content = models.TextField(verbose_name='Blog content', blank=True)
    blog_picture = models.ImageField(
        verbose_name='Blog picture', upload_to='blogs/', null=True, blank=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blog_title


class Appointment(models.Model):

    name = models.CharField(max_length=50, verbose_name='Name', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    phone_number = models.CharField(
        max_length=50, verbose_name='Phone number', blank=True)
    service = models.ForeignKey(
        Service, null=True, verbose_name='Service', on_delete=models.SET_NULL)
    time = models.TimeField(verbose_name='Time', blank=True)
    date = models.DateField(verbose_name='Date', blank=True)
