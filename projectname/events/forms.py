from django import forms
from .models import Person

class RegisterForm(forms.Form):
    error_css_class = 'errorlist'
    
    attendee_first_name = forms.CharField(label='Your First Name', max_length=100)
    attendee_last_name = forms.CharField(label='Your Last Name', max_length=100)
    attendee_email = forms.CharField(label='Your Email', max_length=200)
    
    class Meta:
        model = Person