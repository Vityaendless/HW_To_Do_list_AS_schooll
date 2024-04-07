from django import forms
from .models import Task, Project
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('summary', 'description', 'types', 'status')
        widgets = {'types': forms.SelectMultiple}
        error_messages = {
            'summary': {
                'required': 'Please enter summary',
                'min_length': 'Please write 5 symbols or more'
            }
        }


    # def clean_summary(self):
    #     summary = self.cleaned_data.get('summary')
    #     if summary ...:
    #         raise ValidationError('There is a category with that name')
    #     return summary

    def clean(self):
        cleaned_data = super().clean()
        summary = cleaned_data.get('summary')
        description = cleaned_data.get('description')
        if summary == description:
            raise ValidationError('There are not equals summary and desc')
        return cleaned_data


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'end_date')
        error_messages = {
            'title': {
                'required': 'Please enter title',
                'min_length': 'Please write 5 symbols or more'
            }
        }


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')
