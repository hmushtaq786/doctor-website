from django.urls import path
from doctor_app import views

urlpatterns = [
    path('', views.index),
]
