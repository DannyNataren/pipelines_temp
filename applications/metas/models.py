from django.db import models
from django.core.exceptions import ValidationError
from applications.organizaciones.models import Organizacion


def validate_year_range(value):
    if value < 1950 or value > 2100:
        raise ValidationError('El año debe estar entre 1950 y 2100.')


# Create your models here.
class MetaModel(models.Model):
    anio = models.IntegerField(null=False, validators=[validate_year_range])
    meta = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=False, db_column="fk_meta_x_organizaciones")

    class Meta:
        db_table = "metas"
