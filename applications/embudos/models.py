from django.db import models
from applications.organizaciones.models import Organizacion


# Create your models here.
class Embudo(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    etapas = models.IntegerField(null=False, default=0, db_column="numero_de_etapas")
    esta_activo = models.CharField(null=False, default=True)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=False,
                                     db_column="fk_embudos_x_organizaciones")

    class Meta:
        db_table = "embudos"
