from django import forms
from .models import Appointment


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


# <input type="text" class="contact_input" placeholder="Your Name" required="required">
# 								<input type="email" class="contact_input" placeholder="Your E-mail" required="required">
# 								<input type="tel" class="contact_input" placeholder="Your Phone" required="required">
# 								<select class="contact_select contact_input" required>
# 									<option disabled="" selected="" value="">Service</option>
# 									<option>Abdominoplasty</option>
# 								</select>
# 								<select class="contact_select contact_input"required="required">
# 										<option disabled="" selected="">Time</option>
# 										<option>Morning</option>
# 										<option>Evening</option>
# 									</select>
# 								<input type="text" id="datepicker" class="contact_input datepicker" placeholder="Date" required="required">
