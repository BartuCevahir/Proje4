from django.http import HttpResponse
from django.template import loader

def takimlar(request):
  template = loader.get_template('takimlar.html')
  return HttpResponse(template.render()) 
# Create your views here.
