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


@api_view(['POST'])
def categoriaCreate(request):   
    serializer = CategoriaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    


@api_view(['POST'])
def categoriaUpdate(request, pk):   
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(instance=categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  


@api_view(['DELETE'])
def categoriaDelete(request, pk):   
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()

    return Response('categoria borrado!')  


# def for productos


@api_view(['GET'])
def productoList(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productoDetail(request, pk):
    producto = Producto.objects.get(id=pk)
    serializer = ProductoSerializer(producto, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productoCreate(request):   
    serializer = ProductoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    


@api_view(['POST'])
def productoUpdate(request, pk):   
    producto = Producto.objects.get(id=pk)
    serializer = ProductoSerializer(instance=producto, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  


@api_view(['DELETE'])
def productoDelete(request, pk):   
    producto = Producto.objects.get(id=pk)
    producto.delete()

    return Response('producto borrado!')  


# def for clientes


@api_view(['GET'])
def clienteList(request):
    cliente = Cliente.objects.all()
    serializer = ClienteSerializer(cliente, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def clienteDetail(request, pk):
    cliente = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(cliente, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def clienteCreate(request):   
    serializer = ClienteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    


@api_view(['POST'])
def clienteUpdate(request, pk):   
    cliente = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(instance=cliente, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  


@api_view(['DELETE'])
def clienteDelete(request, pk):   
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()

    return Response('cliente borrado!')  


# def for administrador


@api_view(['GET'])
def administradorList(request):
    administrador = Administrador.objects.all()
    serializer = AdministradorSerializer(administrador, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def administradorDetail(request, pk):
    administrador = Administrador.objects.get(id=pk)
    serializer = AdministradorSerializer(administrador, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def administradorCreate(request):   
    serializer = AdministradorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    


@api_view(['POST'])
def administradorUpdate(request, pk):   
    administrador = Administrador.objects.get(id=pk)
    serializer = AdministradorSerializer(instance=administrador, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  


@api_view(['DELETE'])
def administradorDelete(request, pk):   
    administrador = Administrador.objects.get(id=pk)
    administrador.delete()

    return Response('administrador borrado!')  