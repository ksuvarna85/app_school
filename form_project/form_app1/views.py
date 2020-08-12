from django.shortcuts import render
from form_app1 import forms
def index(request):

    return render(request,'form_app1/index.html')
def formpage(request):
    form=forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("valided")
            print('name:',form.cleaned_data['name'])
            print('email:',form.cleaned_data['email'])
            print('textarea:',form.cleaned_data['text'])

    return render(request,'form_app1/form_page.html',context={'form':form})

# Create your views here.
