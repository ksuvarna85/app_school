from django import forms
from django.core import validators


def check_for_z(value):
    if value[0]!='z':
        raise forms.ValidationError("Name starts with z")

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.CharField()
    verify_email=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("chech ur email")
