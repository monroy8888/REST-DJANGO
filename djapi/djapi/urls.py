"""djapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from djapi.views import saludo, despedida, givemetime, calculaEdad

from api.apiviews import CategoriaSave, SubCategoriaSave

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('init/', saludo),
    path('exit/', despedida),
    path('time/', givemetime),
    path('age/<int:edad>/<int:agno>', calculaEdad),

=======
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
    path('dj-puro/', include('dj_puro.urls')),
    path('api/',include('api.urls')),
    path('v1/categorias/', CategoriaSave.as_view(),name='categoria_save' ),
    path('v1/subcategorias/', SubCategoriaSave.as_view(),name='subcategoria_save' ),
]
