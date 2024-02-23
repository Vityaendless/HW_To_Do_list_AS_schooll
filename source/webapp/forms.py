from django import forms
from django.forms import widgets
from .models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Description')
    full_description = forms.CharField(max_length=3000, label='Full description', widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Status', widget=widgets.Select, choices=status_choices)
    deadline = forms.CharField(max_length=10, label='Deadline')
