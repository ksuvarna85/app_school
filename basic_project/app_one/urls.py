from django.urls import path,include

from app_one import views

app_name='app_one'


urlpatterns=[
    path('register/',views.register,name='register')
]
