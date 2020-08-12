from django.contrib import admin
from django.urls import path,include
from app1 import views

app_name='app1'

urlpatterns=[
    path("",views.name,name='nam'),
    path("maps/",views.map,name="map"),

]
