from django import forms
from .models import Schedule

class ScheForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields={'title', 'content',}