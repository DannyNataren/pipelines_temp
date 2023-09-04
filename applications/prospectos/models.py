from django.db import models
from applications.empresas.models import Empresa
from utils.enums.origenes import OrigenesEnum
from utils.enums.deciones_maker import DecisionesMakerEnum
from utils.enums.puestos import PuestosEnum


# Create your models here.
class Prospecto(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=10, null=False)
    correo = models.CharField(max_length=255, null=False)
    linkedin = models.CharField(max_length=255, null=True)
    origen = models.CharField(
        max_length=255,
        null=False,
        choices=[
            (OrigenesEnum.DESCONOCIDO, "Desconocido"),
            (OrigenesEnum.BNI, "BNI"),
            (OrigenesEnum.BDCOMPRADA, "Base de datos comprada"),
            (OrigenesEnum.CAPWEBSITE, "Capacitación WebSite"),
            (OrigenesEnum.NETWEBINAR, "Networking Webinar"),
            (OrigenesEnum.REFCOLABORADOR, "Referido por colaborador"),
        ]
    )
    detalles_origen = models.CharField(max_length=1000, null=True)
    es_decision_maker = models.CharField(
        max_length=45,
        null=False,
        choices=[
            (DecisionesMakerEnum.SI, "Si",),
            (DecisionesMakerEnum.NO, "No"),
            (DecisionesMakerEnum.DESCONOCIDO, "Desconocido"),
        ]
    )
    puesto = models.CharField(
        max_length=45,
        null=False,
        choices=[
            (PuestosEnum.DESCONOCIDO, "Desconocido"),
            (PuestosEnum.CEO, "CEO",),
            (PuestosEnum.DIRECTOR, "Director",),
            (PuestosEnum.SOCIO, "Socio"),
        ]
    )
    creado_por = models.IntegerField(null=False),
    esta_activo = models.BooleanField(null=False, default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, db_column="fk_prospectos_x_empresas")

    class Meta:
        db_table = "prospectos"
