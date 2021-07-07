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
    path('administrador/categoria-create/', views_core.categoriaCreate, name="categoria-create"), #-->
    path('administrador/categoria-update/<str:pk>/', views_core.categoriaUpdate, name="categoria-update"), #-->
    path('administrador/categoria-delete/<str:pk>/', views_core.categoriaDelete, name="categoria-delete"), #-->


    #productos


    path('cliente/producto-list/', views_core.productoList, name="producto-list"),
    path('cliente/producto-detail/<str:pk>/', views_core.productoDetail, name="producto-detail"),
    #categorias administrador
    path('administrador/producto-create/', views_core.productoCreate, name="producto-create"), #-->
    path('administrador/producto-update/<str:pk>/', views_core.productoUpdate, name="producto-update"), #-->
    path('administrador/producto-delete/<str:pk>/', views_core.productoDelete, name="producto-delete"), #-->


    #clientes

    
    path('cliente-list/', views_core.clienteList, name="cliente-list"),
    path('cliente-detail/<str:pk>/', views_core.clienteDetail, name="cliente-detail"),
    #categorias administrador
    path('cliente-create/', views_core.clienteCreate, name="cliente-create"), #-->
    path('cliente-update/<str:pk>/', views_core.clienteUpdate, name="cliente-update"), #-->
    path('cliente-delete/<str:pk>/', views_core.clienteDelete, name="cliente-delete"), #-->
    

    #administracion

    
    path('administrador-list/', views_core.administradorList, name="administrador-list"),
    path('administrador-detail/<str:pk>/', views_core.administradorDetail, name="administrador-detail"),
    #categorias administrador
    path('administrador-create/', views_core.administradorCreate, name="administrador-create"), #-->
    path('administrador-update/<str:pk>/', views_core.administradorUpdate, name="administrador-update"), #-->
    path('administrador-delete/<str:pk>/', views_core.administradorDelete, name="administrador-delete"), #-->
    
]
