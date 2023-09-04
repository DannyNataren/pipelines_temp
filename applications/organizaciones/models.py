from django.db import models
from applications.membresias.models import Membresia
from utils.enums.tamanios import TamanioEnum
from utils.enums.industrias import IndustriasEnum


class Organizacion(models.Model):
    nombre = models.CharField(max_length=255, null=False, unique=True)
    url = models.CharField(max_length=255, null=False)
    ubicacion = models.CharField(max_length=255, null=False)
    tamanio = models.CharField(
        max_length=255,
        null=False,
        choices=[
            (TamanioEnum.MIC, 'Micro'),
            (TamanioEnum.PEQ, 'Pequeña'),
            (TamanioEnum.MED, "Mediana"),
            (TamanioEnum.GRA, 'Grande')
        ]
    )
    industria = models.CharField(
        max_length=255,
        null=False,
        choices=[
            (IndustriasEnum.GOBERNANZA, "Gobernanza"),
            (IndustriasEnum.TRANSPORTACION, "Transportación"),
            (IndustriasEnum.SEGURIDAD, "Seguridad"),
            (IndustriasEnum.SOFTWARE, "Software"),
            (IndustriasEnum.LEGAL, "Legal"),
            (IndustriasEnum.LOGISTICA, "Logística"),
            (IndustriasEnum.SALUD, "Salud"),
            (IndustriasEnum.EDUCACION, "Educación")
        ]
    )
    especialidad = models.CharField(max_length=1000)
    esta_activo = models.BooleanField(null=False, default=True)
    membresia = models.ForeignKey(Membresia, null=True, on_delete=models.SET_NULL, db_column="fk_organizaciones_x_membresias")

    class Meta:
        db_table = "organizaciones"
