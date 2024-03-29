from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('summary', 'description', 'types', 'status')
        widgets = {'types': forms.SelectMultiple}
        error_messages = {
            'summary': {
                'required': 'Please enter summary',
                'min_length': 'Please write 10 symbols or more'
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
