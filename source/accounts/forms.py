from django.contrib.auth.forms import UserCreationForm
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if first_name == "" or last_name == "":
            raise forms.ValidationError('Last name or first name are empty.')
