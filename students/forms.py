from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'roll_number', 'class_name', 'phone', 'address']