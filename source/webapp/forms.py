from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Description')
    full_description = forms.CharField(max_length=3000, label='Full description', widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Status', widget=widgets.Select, choices=status_choices)
    deadline = forms.CharField(max_length=10, label='Deadline')

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 5:
            raise ValidationError('Need length more than 5 symbols')
        return description

    def clean(self):
        description = self.cleaned_data.get('description')
        full_description = self.cleaned_data.get('full_description')
        if description == full_description:
            raise ValidationError('Description and full description couldnt be equal')
        return super().clean()
