from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kurulüyeleri(request):
    return HttpResponse("Kurul üyeleri sitemize hoş geldiniz.")



