from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader # yeni eklenen

# Create your views here.

def kurulüyeleri(request):

    gidecek = loader.get_template('kuruluyeleri.html') # yeni eklenen
    return HttpResponse(gidecek.render()) # yeni eklenen
