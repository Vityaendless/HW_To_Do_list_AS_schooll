from django import forms
from django.forms import widgets
from .models import Type, Status
from django.core.exceptions import ValidationError


class TaskForm(forms.Form):
    summary = forms.CharField(min_length=10 ,max_length=50, label='Summary')
    description = forms.CharField(max_length=3000, required=False, label='Description', widget=widgets.Textarea)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status')

    # def clean_summary(self):
    #     summary = self.cleaned_data.get('summary')
    #     if summary ...:
    #         raise ValidationError('There is a category with that name')
    #     return summary
