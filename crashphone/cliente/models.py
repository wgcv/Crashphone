# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, unique=True)
	foto = models.ImageField(upload_to='profile_images', blank=True,null=True)
	celular = models.CharField("Número de celular", max_length=20)
	"""nombre = models.CharField("Nombre del cliente", max_length=150)
	direccion = models.CharField("Directorio del cliente", max_length=150)
	lon = models.FloatField()
	lat = models.FloatField()"""
	def __str__(self):
		return self.user.username