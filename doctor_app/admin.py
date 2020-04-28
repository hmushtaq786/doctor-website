from django.contrib import admin
from .models import Subscriber, ClientTestimonial, FAQ, Service, Blog, Appointment

# Register your models here.

admin.site.register(Subscriber)
admin.site.register(ClientTestimonial)
admin.site.register(FAQ)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Appointment)
