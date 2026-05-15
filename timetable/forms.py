# timetable/forms.py

from django import forms
from .models import Timetable


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [
            'course',
            'subject',
            'day',
            'start_time',
            'end_time',
            'room',
        ]

        widgets = {
            'course': forms.Select(attrs={
                'class': 'form-control'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject name'
            }),

            'day': forms.Select(attrs={
                'class': 'form-control'
            }),

            'start_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'end_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'room': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room number'
            }),
        }