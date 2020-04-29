from django.urls import path
from doctor_app import views


# TEMPLATE TAGGING
app_name = 'doctor_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
