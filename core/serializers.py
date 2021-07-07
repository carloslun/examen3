from rest_framework import serializers
from .models import Categoria, Cliente, Producto, Administrador

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        fields = '__all__'


class AdministradorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Administrador
        fields = '__all__'



        