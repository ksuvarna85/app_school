from django.urls import path,include
from first_app import views

app_name='first_app'

urlpatterns=[
    path("",views.SchoolListView.as_view(),name='school_list'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name='details'),
    path('create/',views.SchoolCreateView.as_view(),name="create"),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),

]
