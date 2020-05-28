from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apiviews import ProductoList, ProductoDetalle, \
    CategoriaList, SubCategoriaList, SubCategoriaAdd, ProductoViewSet, \
    UserCreate

<<<<<<< HEAD
#router = DefaultRouter()
#router.register('v2/productos', ProductoViewSet, base_name = 'productos')
=======
router = DefaultRouter()
router.register('v2/productos/', ProductoViewSet, base_name='productios')
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),
    path('v1/categorias/', CategoriaList.as_view(),name='categoria_save' ),
    #path('v1/subcategorias/<int:pk>', SubCategoriaList.as_view(),name='subcategoria_save' ),
    path('v1/categorias/<int:pk>/categorias/', CategoriaList.as_view(), name='categoria_detalle' ),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list' ),

    path('v1/categorias/<int:pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='sc_add' ),

    path('v3/usuarios/', UserCreate.as_view(),name='usuario_crear'),
    ]

<<<<<<< HEAD
# urlpatterns += router.urls
=======
urlpatterns += router.urls
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
