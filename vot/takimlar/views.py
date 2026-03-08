from django.http import HttpResponse
from django.template import loader

def takimlar(request):
  template = loader.get_template('takimlar.html')
  return HttpResponse(template.render()) 
# Create your views here.

def erkektakimi(request):
  template = loader.get_template('erkektakimi.html')
  return HttpResponse(template.render()) 

def kadintakimi(request):
  template = loader.get_template('kadintakimi.html')
  return HttpResponse(template.render()) 