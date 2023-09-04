from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class DetallesUsuario(models.Model):
    telefono = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column="auth_user_id")

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "detalles_usuarios"
