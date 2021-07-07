from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Cliente, Producto, Administrador
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, AdministradorSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# def for categoria


@api_view(['GET'])
def categoriaList(request):
    categoria = Categoria.objects.all()
    serializer = CategoriaSerializer(categoria, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoriaDetail(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(categoria, many=False)
    return Response(serializer.data)

# def for productos


@api_view(['GET'])
def productoList(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)




