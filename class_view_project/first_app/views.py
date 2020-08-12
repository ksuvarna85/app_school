from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from first_app.models import School,Student
from django.urls import reverse_lazy
class IndexView(TemplateView):
    template_name='index.html'

# Create your views here.
class SchoolListView(ListView):
    context_object_name='schools'
    model=School


class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=School
    template_name='first_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=School
class SchoolDeleteView(DeleteView):
    model=School
    success_url=reverse_lazy("first_app:school_list")
