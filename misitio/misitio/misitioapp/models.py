from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha = models.DateTimeField('Fecha que la publicamos')

class Correct(models.Model):
	pregunta = models.ForeignKey(Pregunta)
	texto_opcion = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

class Opcion2(models.Model):
	pregunta = models.ForeignKey(Pregunta)
	texto_opcion = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)