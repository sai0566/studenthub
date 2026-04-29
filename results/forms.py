from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['subject', 'marks', 'total_marks']