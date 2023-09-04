from django.db import models
from django.contrib.auth.models import User
from applications.etapas.models import Etapa


# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=1000, null=True)
    esta_activo = models.BooleanField(default=True, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column="fk_proyectos_x_auth_user")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, null=False, db_column="fk_proyectos_x_etapas")

    class Meta:
        db_table = "proyectos"


class HistorialProyecto(models.Model):
    etapa = models.IntegerField(null=False)
    dias_etapa = models.IntegerField(null=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column="fk_historial_proyectos_x_proyectos")

    class Meta:
        db_table = "historial_proyectos"

