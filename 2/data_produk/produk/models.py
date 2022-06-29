from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100, default=None)
    deskripsi = models.TextField()
    harga = models.PositiveIntegerField(default=None)
    gambar = models.CharField(max_length=500)
    timestamp = models.CharField(max_length=64)
