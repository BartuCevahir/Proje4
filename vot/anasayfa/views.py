from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def anasayfa_tr(request):
  template = loader.get_template('ana.html')
  return HttpResponse(template.render())


# def anasayfa_tr(request):
#     return HttpResponse("Web sitesine hoş geldiniz.")

def anasayfa_f_en(request):
    return HttpResponse("Welcome my website.")
