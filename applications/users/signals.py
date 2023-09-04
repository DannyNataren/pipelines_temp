from django.contrib.auth.models import Group


try:
    grupo_administradores = Group.objects.get_or_create(name="Administradores")
    grupo_gerentes = Group.objects.get_or_create(name="Gerentes de ventas")
    grupo_vendedores = Group.objects.get_or_create(name="Vendedores")
except:
    pass