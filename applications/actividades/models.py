from django.db import models
from applications.proyectos.models import Proyecto
from utils.enums.tipos import TiposEnum


# Create your models here.
class Actividad(models.Model):
    descripcion = models.CharField(null=False, max_length=1000)
    tipo = models.CharField(
        max_length=45,
        choices=[
            (TiposEnum.LLAMADA, 'Llamada'),
            (TiposEnum.CORREO, 'Correo electrónico'),
            (TiposEnum.REUNION, 'Reunión'),
        ],
        null=False
    )
    fecha_actividad = models.DateTimeField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    hay_evento_calendar = models.BooleanField(null=False, default=True)
    esta_activo = models.BooleanField(null=False, default=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column="fk_actividades_x_proyectos")

    class Meta:
        db_table = "actividades"
