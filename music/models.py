from django.db import models

# Create your models here.

class Banda(models.Model):
	nome = models.CharField(max_length=50)
	musicos = models.ManyToManyField('Musico')
	estilo = models.ForeignKey('EstiloMusical', on_delete=models.CASCADE)
	criacao = models.DateField(default=None, blank=True, null=True)
	
	def __str__	(self):
		return self.nome

class Musico(models.Model):
	nome = models.CharField(max_length=20)
	sobrenome = models.TextField()
	nascimento = models.DateField(default=None, blank=True, null=True)
	email = models.EmailField(default=None, blank=True, null=True)
	genero = models.CharField(max_length=1,default=None, blank=True, null=True)

	def __str__	(self):
		return self.nome


class EstiloMusical(models.Model):
	nome = models.CharField(max_length=100)
	bandas = models.ManyToManyField('Banda')

	def __str__	(self):
		return self.nome

