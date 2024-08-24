from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # ID de Usuario
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    id = models.AutoField(primary_key=True)  # ID de Nivel
    tipo_nivel = models.CharField(max_length=50)

    class Meta:
        db_table = 'Nivel'
    
    def __str__(self):
        return self.tipo_nivel

class Puntuaje(models.Model):
    id = models.AutoField(primary_key=True)  # ID de Puntuaje
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    puntuaje = models.IntegerField()
    tiempo = models.CharField(max_length=10)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)  # Relación con Nivel

    class Meta:
        db_table = 'Puntuaje'
    
    def __str__(self):
        return f"{self.nombre} - {self.puntuaje}"
