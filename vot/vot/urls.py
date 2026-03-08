"""
URL configuration for vot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import anasayfa.views
import kurulüyeleri.views
import üyeler.views
import etkinlikler.views
import takimlar.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', anasayfa.views.anasayfa_f_en),  
    path('anasayfa/', anasayfa.views.anasayfa_tr), 
    path('', anasayfa.views.anasayfa_tr), 
    path('kurulüyeleri/', kurulüyeleri.views.kurulüyeleri, name='kurulüyeleri'),
    path('üyeler/', üyeler.views.uyeler_tr),
    path('kurulüyeleri/detay/<int:gelenid>', kurulüyeleri.views.detay, name='detay'),
    path('kurulüyeleri/sil/<int:gelenid>', kurulüyeleri.views.sil, name='CRUD_sil'),
    path('kurulüyeleri/ekle', kurulüyeleri.views.ekle),
    path('kurulüyeleri/guncelle/<int:gelenid>', kurulüyeleri.views.guncelle, name='kurulüyeleriduzelt'),
    path('etkinlikler/', etkinlikler.views.etkinlikler, name = 'etkinlikler'),
    path('takimlar/', takimlar.views.takimlar, name = 'takimlar'),
    # path('takimlar/erkektakimi/<int:gelenid>', takimlar.views.erkektakimi), 
    path('takimlar/erkektakimi/', takimlar.views.erkektakimi), 
    path('takimlar/kadintakimi/', takimlar.views.kadintakimi), 


]
