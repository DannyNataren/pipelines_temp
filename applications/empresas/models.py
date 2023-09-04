from django.db import models
from applications.organizaciones.models import Organizacion
from utils.enums.tamanios import TamanioEnum
from utils.enums.industrias import IndustriasEnum
from utils.enums.tiposEmpresa import TiposEmpresaEnum


class Empresa(models.Model):
    nombre = models.CharField(max_length=45, null=False)
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
    tipo_empresa = models.CharField(
        max_length=255,
        null=False,
        choices=[
            (TiposEmpresaEnum.COMPETENCIA, 'Competencia'),
            (TiposEmpresaEnum.ALIADO, 'Aliado'),
            (TiposEmpresaEnum.CLIENTE, 'Cliente')
        ]
    )
    creado_por = models.IntegerField(null=False)
    esta_activo = models.BooleanField(null=False, default=True)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=False, db_column="fk_empresas_x_organizaciones")

    class Meta:
        db_table = "empresas"

