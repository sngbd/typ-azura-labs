from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Produk
from .forms import FormProduk


def index(request):
    produk = Produk.objects.all()
    return render(request, "produk/index.html", {
        "title": "Daftar Produk",
        "items": produk
    })


def buat(request):
    if request.method == 'POST':
        form = FormProduk(request.POST)
        if form.is_valid():
            produk = Produk(
                nama = form.cleaned_data['nama'],
                deskripsi = form.cleaned_data['deskripsi'],
                harga = form.cleaned_data['harga'],
                gambar = form.cleaned_data['gambar'],
                timestamp = timezone.localtime().strftime("%B %d, %Y, %I:%M%p")
            )
            produk.save()
            return HttpResponseRedirect(reverse('produk:index'))
    else:
        return render(request, "produk/buat.html", {
            "form": FormProduk
        })


def produk(request, id):
    data = Produk.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect(reverse('produk:index'))
    return render(request, "produk/produk.html", {
        "data": data,
    })


def edit(request, id):
    produk = Produk.objects.get(id=id)
    if request.method == "POST":
        form = FormProduk(request.POST)
        if form.is_valid():
            produk.nama = form.cleaned_data['nama']
            produk.deskripsi = form.cleaned_data['deskripsi']
            produk.harga = form.cleaned_data['harga']
            produk.gambar = form.cleaned_data['gambar']
            produk.save()
            return HttpResponseRedirect(reverse('produk:index'))
    data = {
        'nama': produk.nama, 
        'deskripsi': produk.deskripsi, 
        'harga': produk.harga, 
        'gambar': produk.gambar
    }
    form = FormProduk(initial=data)
    return render(request, "produk/edit.html", {
        "form": form,
        "id": id
    })