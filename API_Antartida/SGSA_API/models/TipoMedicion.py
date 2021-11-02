from django.db import models

from API_Antartida.SGSA_API.models.Lectura import Lectura


class TipoMedicion(models.Model):
    # idTipoMedicion=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    unidad=models.CharField(max_length=30)
    
