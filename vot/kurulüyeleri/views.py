from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from django.http import HttpResponse 
from django.template import loader # yeni eklenen
from .models import Kurulüyeleri
from django.shortcuts import get_object_or_404



# Create your views here.

def kurulüyeleri(request):

    kurulüyeleriliste = Kurulüyeleri.objects.all()
    sayfa = loader.get_template('kuruluyeleri.html')
    gidecek ={
        'kurulüyeleriliste' : kurulüyeleriliste,
    }
    print(kurulüyeleriliste)
    return HttpResponse(sayfa.render(gidecek, request))

   
def detay(request, gelenid):
  secilen = Kurulüyeleri.objects.get(id=gelenid)
  sayfa = loader.get_template('kurulüyeleridetay.html')
  gidecek = {
    'giden': secilen,
  }
  return HttpResponse(sayfa.render(gidecek, request))

def sil(request, gelenid):
  item = Kurulüyeleri.objects.get(id=gelenid)
  item.delete()
  return redirect('kurulüyeleri') 


class KurulüyeleriForm(forms.ModelForm):
    class Meta:
        model = Kurulüyeleri
        fields = ['Sıra', 'AdiSoyadi',
                  'Mevki']  
# Kullanmak istediğiniz alanları buraya ekleyin

def ekle(request):
    if request.method == 'POST': # POST = Gönderme işlemi
        form = KurulüyeleriForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('kurulüyeleri')  #url name
    else: # GET işlemi
        form = KurulüyeleriForm()
    return render(request, 'kurulüyeleriekle.html', {'form': form})

   
def guncelle(request, gelenid):
    # kurulüyelerinesnesi = get_object_or_404(Kurulüyeleri, id=gelenid)
    kurulüyelerinesnesi = Kurulüyeleri.objects.get(id=gelenid)
    if request.method == 'POST':
        form = KurulüyeleriForm(request.POST, instance=kurulüyelerinesnesi)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('kurulüyeleri') #url name
    else:
        form = KurulüyeleriForm(instance=kurulüyelerinesnesi)
    return render(request, 'kurulüyeleriguncelle.html', {'form': form}) 

   
