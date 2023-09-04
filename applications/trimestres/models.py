from django.db import models
from applications.metas.models import MetaModel


# Create your models here.
class Trimestre(models.Model):
    trimestre = models.IntegerField(null=False)
    oportunidades = models.IntegerField(null=False)
    prospectos = models.IntegerField(null=False)
    ventas = models.IntegerField(null=False)
    meta = models.ForeignKey(MetaModel, on_delete=models.CASCADE, null=False, db_column="fk_trimestres_x_metas")

    class Meta:
        db_table = "trimestres"

