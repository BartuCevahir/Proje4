from django.contrib import admin

from .models import Kurulüyeleri


class KurulüyeleriAdmin(admin.ModelAdmin):
  list_display = ("AdiSoyadi", "Mevki")
 
admin.site.register(Kurulüyeleri, KurulüyeleriAdmin)

