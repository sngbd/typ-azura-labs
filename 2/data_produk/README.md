# Aplikasi Data Produk Deskripsi

## Dependensi
- Python3

## Menjalankan Aplikasi
Untuk menjalankan aplikasi web ini, saya sarankan untuk membuat virtual environment 
terlebih dahulu sebagai berikut (macOS/Linux):
```
python -m venv .venv
source .venv/bin/activate
```
Kemudian install dependensi program:
```
pip install -r requirements.txt
```
Migrasi database dengan melakukan:
```
python manage.py makemigrations
python manage.py migrate
```
Lalu, program bisa dijalankan dengan:
```
python manage.py runserver
```