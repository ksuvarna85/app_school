from django.shortcuts import render
import requests
from app1.models import NameOfPerson
# Create your views here.
def map(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('https://freegeoip.app/json/%s' % ip_address)
    #response = requests.get('https://freegeoip.app/json/')
    geodata = response.json()


    return render(request, 'app1/map.html', {

         'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],

    })

def index(request):
    return render(request,'app1/index.html')

def name(request):
    if request.method=="POST":
        name=request.POST.get('name_sent')
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('https://freegeoip.app/json/%s' % ip_address)
        geodata = response.json()
        country= geodata['country_name']

        model=NameOfPerson.objects.all()
        course=model




        #name=request.POST.get('name_sent')
        x=NameOfPerson(name_person=name,count=0)
        y=x.count
        y=y+1
        x=NameOfPerson(name_person=name,count=y)



        check=NameOfPerson.objects.filter(name_person=x).exists()

        if(check==False):
            y=x.count
            y=y+1
            x.save()





        return render(request,'app1/name.html',{
            'name':name,
            'ip': geodata['ip'],
            'country': geodata['country_name'],
        })
    else:
        return render(request,'app1/name.html')
