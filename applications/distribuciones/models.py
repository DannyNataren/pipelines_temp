from django.db import models
from django.contrib.auth.models import User
from applications.trimestres.models import Trimestre


# Create your models here.
class Distribucion(models.Model):
    oportunidades = models.IntegerField(null=False)
    prospectos = models.IntegerField(null=False)
    ventas = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column="fk_distribuciones_x_auth_user")
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, null=False, db_column="fk_distribuciones_x_trimestres")

    class Meta:
        db_table = "distribuciones"

