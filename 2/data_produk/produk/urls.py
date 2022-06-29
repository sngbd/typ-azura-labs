from django.urls import path

from . import views

app_name = "produk"
urlpatterns = [
    path("", views.index, name="index"),
    path("buat", views.buat, name="buat"),
    path("edit", views.edit, name="edit"),
    path("produk/<str:id>/", views.produk, name="produk"),
    path("edit/<str:id>/", views.edit, name="edit"),
]
