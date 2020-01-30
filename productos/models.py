# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Soil(models.Model):
    attribute = models.CharField(max_length=40, unique=True)
    soil1 = models.CharField(max_length=40,blank=True)
    soil2 = models.CharField(max_length=40, blank=True)
    soil3 = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.descripcion

class Irrigation(models.Model):
    attribute = models.CharField(max_length=40, unique=True)
    irri1 = models.CharField(max_length=40,blank=True)
    irri2 = models.CharField(max_length=40, blank=True)
    irri3 = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    attribute = models.CharField(max_length=100, unique=True)
    crop1 = models.CharField(max_length=40,blank=True)
    crop2 = models.CharField(max_length=40, blank=True)
    crop3 = models.CharField(max_length=40, blank=True)
    # crop2 = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    # crop3 = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

class Proveedor(models.Model):
    ruc = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    correo = models.EmailField(null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add=True)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=5,decimal_places=2)