from django import forms
from .models import Todayspecial

class TodayspecialForm(forms.ModelForm):
    class Meta:
        model = Todayspecial
        fields = ['restaurant', 'name', 'description', 'image']
