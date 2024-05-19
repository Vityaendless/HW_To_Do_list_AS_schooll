from django.contrib.auth.forms import UserCreationForm
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        #cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not first_name or not last_name:
            raise forms.ValidationError('Last name or first name are empty.')
        #return cleaned_data
