from django import forms
from django.core import validators

def positive(value):
    if int(value)<0 :
        raise forms.ValidationError("Enter Positive nos")
def integer(value):
    if value[0]>='a' and value[0]<=z or value[0]>='A' and value[0]<='Z':
        raise forms.ValidationError("Enter a no")



class InputNos(forms.Form):
    Lower_limit=forms.CharField(validators=[positive,integer])
    Upper_limit=forms.CharField(validators=[positive,integer])
