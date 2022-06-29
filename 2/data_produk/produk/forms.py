from django import forms


class FormProduk(forms.Form):
    nama = forms.CharField(label='', max_length=100, widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Nama',
       }))
    deskripsi = forms.CharField(label='', widget=forms.Textarea(
       attrs={
           'class': 'form-control',
           'placeholder': 'Deskripsi',
       }))
    harga = forms.IntegerField(min_value = 0, label='', widget=forms.NumberInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Harga',
       }))
    gambar = forms.CharField(max_length=1000, required=True, label='', widget=forms.TextInput(
        attrs={
           'class': 'form-control',
           'placeholder': 'Gambar',
        }))
