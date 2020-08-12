from django.shortcuts import render
import requests
from app1.models import Name
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
        #name=request.POST.get('name_sent')
        x=Name(name_person=name)
        x.save()
        #y=CountryName(name_foreign=x,country_name=country,count=0)
        #y.save()



        return render(request,'app1/name.html',{
            'name':name,
            'ip': geodata['ip'],
            'country': geodata['country_name'],
        })
    else:
        return render(request,'app1/name.html')
