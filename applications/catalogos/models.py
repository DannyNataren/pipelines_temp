from django.db import models
from applications.organizaciones.models import Organizacion
from applications.tipos_catalogos.models import TipoCatalogo


# Create your models here.
class Catalogo(models.Model):
    nombre_origen = models.CharField(max_length=255, null=False)
    creado_por = models.IntegerField(null=False)
    tipo_catalogo = models.ForeignKey(TipoCatalogo, on_delete=models.CASCADE, null=False, db_column="fk_catalogos_x_tipos_catalogos")
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=False, db_column="fk_catalogos_x_organizaciones")

    class Meta:
        db_table = "catalogos"

