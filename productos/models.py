# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.TextField(default='',
                             blank=True)

class General(models.Model):
    farmName = models.CharField(max_length=40, unique=True)
    soil1 = models.CharField(max_length=40,blank=True)
    soil2 = models.CharField(max_length=40, blank=True)
    soil3 = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.descripcion

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


class FarmSettings(models.Model):
    """
    class for storing the settings of the farm at a given date
    Attributes
        farmId: the identifier of the farm
        farmLabel: the label to show for this farm (can be edited)
        comment: whatever explanation
        active: boolean to activate/deactivate any activity on this farm
        timeZone: name of timezone used for formatting the dates to the users of this farm
        altitude: mean altitude above see level, m
        coordinates: point with longitude, latitude, in degrees
        polygon: Polygon (list of points) representing the contour of the farm
        team: Group of propietaries
        meteoSettings: list of settings available for this farm (relation n:m)
        devices: list of devices deployed in this farm
        tags: free list of tags, each with some meaning for the FrontEnd??????? (Frontend has no domain!) or the BackEnd
        creationDate: Datetime of creation of the entity
        revisionDate: Datetime of modification of the entity
        modifiedBy: User who has modified it


    """
    # farm = models.ForeignKey(Farm, blank=False, null=False, on_delete=models.CASCADE, related_name='settings')
    farm = models.TextField('Comment', blank=True, null=True)
    comment = models.TextField('Comment', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    timeZone = models.CharField(blank=True, null=True, max_length=20, default='CEST')
    altitude = models.FloatField(blank=True, null=True)
    # coordinates = PointField(blank=True, null=True)
    coordinates =models.TextField('Comment', blank=True, null=True)
    # polygon = MultiPolygonField(blank=True, null=True)
    polygon = models.TextField('Comment', blank=True, null=True)
    # meteoSettings = models.ManytoManyField(meteoSettings, blank=False, null=False, on_delete=models.CASCADE, related_name='settings')
    # tags = models.ManytoManyField(tags, blank=False, null=False, on_delete=models.null, related_name='settings')

    creationDate = models.DateTimeField(default=timezone.now, editable=False)
    revisionDate = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):

        """ On Save Update modifiedBy"""
        user = "Mollerussa"
        if user and not user.pk:
            user = None
        self.modifiedBy = user

        """ On Save Update Timestamps"""
        if not self.pk:
            self.creationDate = timezone.now()
        self.revisionDate = timezone.now()

        return super(FarmSettings, self).save(*args, **kwargs)

    def __str__(self):
        return u"%s (%s)" % (self.farm, self.revisionDate)

    class Meta:
        verbose_name = "Farm Settings"
        verbose_name_plural = "Farms Settings"