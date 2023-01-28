from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import plan
from . forms import Myplan
# Create your views here.
class regi(CreateView):
    form_class = Myplan
    template_name= 'myapp/home.html'
    success_url='/thanx/'
class thanx(TemplateView):
    template_name='myapp/thanx.html'