from django import forms
from first_app.models import Webpage,Topic,AccessRecords

class NewUserForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields="__all__"
