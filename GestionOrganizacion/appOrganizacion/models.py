from django.db import models
import os 

# Create your models here.


class Persona(models.Model):
    perIdentificacion = models.CharField(
        max_length=10, unique=True, db_comment="Identificacion de la persona")
    perNombres = models.CharField(
        max_length=70, null=True, db_comment="Nombres de la persona")
    perApellidos = models.CharField(
        max_length=70, null=True, db_comment="Apellidos de la persona")
    perCorreo = models.CharField(
        max_length=70, unique=True, db_comment="Correo de la persona")
    perNumeroCelular = models.CharField(
        max_length=10, unique=True, db_comment="Numero de celular de la persona")

    def __str__(self):
        return f"Identificacion:{self.perIdentificacion} -Nombres: {self.perNombres} -Apellidos:{self.perApellidos} -Correo:{self.perCorreo} -Celular:{self.perNumeroCelular}"
    
class Donacion(models.Model):
    nombreDonador = models.ForeignKey(Persona, on_delete=models.PROTECT, db_comment="Hace relación al donador FK")
    valorDonacion = models.IntegerField(db_comment="Cantidad a Donar")
    fechaDonacion = models.DateTimeField(
        auto_now_add=True, db_comment="Fecha y Hora de la donacion")