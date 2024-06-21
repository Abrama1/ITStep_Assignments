from django import forms
from .models import Attendee, Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Please Enter The Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': 'Please Enter The Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control mt-2', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Please Enter The Location'}),
        }


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mt-2", "placeholder": "Enter name"}),
            "email": forms.EmailInput(attrs={"class": "form-control mt-2", "placeholder": "Enter email"})
        }
