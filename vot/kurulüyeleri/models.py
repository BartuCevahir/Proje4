from django.db import models

class Kurulüyeleri(models.Model):
  
  Sıra = models.CharField(max_length=2)
  AdiSoyadi = models.CharField(max_length=50)
  Mevki = models.CharField(max_length=50)
  


def __str__(self):
        return f"{self.AdiSoyadi} {self.Mevki}"
  
