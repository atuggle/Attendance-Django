from django import forms
from .models import Person

class RegisterForm(forms.Form):
    error_css_class = 'errorlist'
    
    attendee_name = forms.CharField(label='Your Name', max_length=200)
    attendee_email = forms.CharField(label='Your Email', max_length=200)
    
    class Meta:
        model = Person