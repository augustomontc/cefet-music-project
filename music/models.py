from django.db import models

# Create your models here.

class Banda(models.Model):
	nome = models.CharField(max_length=50)
	musicos = models.ManyToManyField('Musico')
	estilo = models.ForeignKey('EstiloMusical', on_delete=models.CASCADE)

class Musico(models.Model):
	nome = models.CharField(max_length=20)
	sobrenome = models.TextField()
	nascimento = models.DateField()


class EstiloMusical(models.Model):
	nome = models.CharField(max_length=100)
	bandas = models.ManyToManyField('Banda')

