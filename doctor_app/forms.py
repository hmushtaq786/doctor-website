from django import forms
from .models import Appointment, Subscriber


class AppointmentForm(forms.ModelForm):

    TITLE_CHOICES = [
        (0, 'Time'),
        (1, 'Morning'),
        (1, 'Evening'),
    ]

    name = forms.CharField(label=False, required=True, widget=forms.TextInput(
        attrs={'class': 'contact_input', 'placeholder': 'Your name'}))

    email = forms.EmailField(label=False, required=True, widget=forms.TextInput(
        attrs={'class': 'contact_input', 'placeholder': 'Your email'}))

    phone_number = forms.CharField(label=False, required=True, widget=forms.TextInput(
        attrs={'class': 'contact_input', 'placeholder': 'Your phone number'}))

    time = forms.ChoiceField(label=False, choices=TITLE_CHOICES, widget=forms.Select(
        attrs={'class': 'contact_input contact_select', 'placeholder': 'Time'}))

    date = forms.DateField(label=False, required=True, widget=forms.TextInput(
        attrs={'id': 'datepicker', 'class': 'contact_input datepicker', 'placeholder': 'Date'}))

    class Meta:
        model = Appointment
        fields = '__all__'


class SubscriberForm(forms.ModelForm):

    email = forms.EmailField(label=False, required=True, widget=forms.TextInput(
        attrs={'class': 'newsletter_input', 'placeholder': 'Your email', 'required': "required"}))

    class Meta:
        model = Subscriber
        fields = '__all__'
