from django.db import models


# Create your models here.
class TipoCatalogo(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = "tipos_catalogos"
