from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'})
        }