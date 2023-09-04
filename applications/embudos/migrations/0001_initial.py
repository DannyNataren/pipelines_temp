# Generated by Django 4.2.4 on 2023-09-03 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizaciones', '0003_organizacion_esta_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('etapas', models.IntegerField(db_column='numero_de_etapas', default=0)),
                ('organizacion', models.ForeignKey(db_column='fk_embudos_x_organizaciones', on_delete=django.db.models.deletion.CASCADE, to='organizaciones.organizacion')),
            ],
        ),
    ]
