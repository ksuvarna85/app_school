from django.shortcuts import render
from app1.forms import InputNos
from app1.code import func1
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    if request.method=="POST":
        form=InputNos(request.POST)
        if form.is_valid():
            num1=int(form.cleaned_data['Number1'])
            num2=int(form.cleaned_data['Number2'])
            result=func1(num1,num2)
            return HttpResponse( json.dumps(result) )
    else:
        form=InputNos()
    return render(request,'app1/index.html',context={'form':form})
