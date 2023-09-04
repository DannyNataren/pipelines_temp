from django.db import models


# Create your models here.
class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    total_vendedores = models.IntegerField(default=0)
    evento_calendario = models.BooleanField(db_column="hay_evento_calendario", default=False)
    precio = models.FloatField()
    esta_activo = models.BooleanField(default=True)
    total_embudos = models.IntegerField(default=0)

    class Meta:
        db_table = "membresias"
