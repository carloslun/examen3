"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views as views_core

urlpatterns = [
    path('admin/', admin.site.urls),
    #categorias
    path('cliente/categoria-list/', views_core.categoriaList, name="categoria-list"),
    path('cliente/categoria-detail/<str:pk>/', views_core.categoriaDetail, name="categoria-detail"),
    #categorias administrador
    path('administrador/categoria-create', views_core.categoriaCreate, name="categoria-create"), #-->
    path('administrador/categoria-update/<str:pk>/', views_core.categoriaUpdate, name="categoria-update"), #-->
    path('administrador/categoria-delete/<str:pk>/', views_core.categoriaDelete, name="categoria-delete"), #-->
    


    #productos
    path('cliente/producto-list/', views_core.productoList, name="producto-list"),
    path('cliente/producto-detail/<str:pk>/', views_core.productoDetail, name="producto-detail"),

]
