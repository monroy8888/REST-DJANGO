from django.urls import path
from .views import categoria_list, categoria_detalle

urlpatterns = [
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/<int_pk>', categoria_detalle, name = 'categorias_detalle')
]
