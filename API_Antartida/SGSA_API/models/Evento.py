from django.db import models
from API_Antartida.SGSA_API.models.Sensor import Sensor

from API_Antartida.SGSA_API.models.TipoEvento import TipoEvento
from API_Antartida.SGSA_API.models.Usuario import Usuario

class Evento(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=300)
    usuario=models.ForeignKey(Usuario , null=True, blank=True)
    sensor=models.ForeignKey(Sensor , null=True, blank=True)
    fecha=models.DateTimeField(auto_now_add= False)
    tipoEvento=models.ForeignKey(TipoEvento)