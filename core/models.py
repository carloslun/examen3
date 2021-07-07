from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    rut = models.CharField(max_length=11) 
    razon_social = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Administrador(models.Model):
    nombre_completo = models.CharField(max_length=90)
    numero_local = models.IntegerField(default=0)


    def __str__(self):
        return self.nombre_completo

    def __unicode__(self):
        return self.nombre_completo


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    descripcion_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

    def __unicode__(self):
        return self.nombre_categoria


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre_producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=60)


    def __str__(self):
        return self.nombre_producto

    def __unicode__(self):
        return self.nombre_producto


