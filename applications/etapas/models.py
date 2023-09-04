from django.db import models
from applications.embudos.models import Embudo


# Create your models here.
class Etapa(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    esta_activo = models.BooleanField(default=True, null=False)
    embudo = models.ForeignKey(Embudo, on_delete=models.CASCADE, null=False, db_column="fk_etapas_x_embudos")

    class Meta:
        db_table = "etapas"

