# -*- encoding: utf-8 -*-
from django.db import models
from cliente.models import Cliente

# Create your models here.

class Tecnico(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField("Nombre del tecnico", max_length=150)
	direccion = models.CharField("Directorio del tecnico", max_length=150)
	celular = models.CharField("Celúlar", max_length=150)
	lon = models.FloatField()
	lat = models.FloatField()
	def __str__(self):
		return self.nombre

class Cita(models.Model):
	id = models.AutoField(primary_key=True)
	idTecnico = models.ForeignKey(Tecnico, unique=False)
	idCliente = models.ForeignKey(Cliente, unique=False)
	direccion = models.CharField("Directorio del tecnico", max_length=150)
	dedescripcionDano = models.CharField("Datos del dano", max_length=150)
	descripcion = models.CharField("Descripcion", max_length=150)
	lon = models.FloatField()
	lat = models.FloatField()
	def __str__(self):
		return self.dedescripcionDano