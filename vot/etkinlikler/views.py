from django.http import HttpResponse
from django.template import loader

def etkinlikler(request):
  template = loader.get_template('etkinlikler.html')
  return HttpResponse(template.render()) 


# Create your views here.
