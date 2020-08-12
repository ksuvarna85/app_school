from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecords
from first_app.forms import NewUserForm

# Create your views here.
def user(request):
    return render (request,'first_app/index.html')

def index(request):
    form=NewUserForm
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("form invalid")
            return user(request)
    return render(request,'first_app/indexog.html',{'form':form})
