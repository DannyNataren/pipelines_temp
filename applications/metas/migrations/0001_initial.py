# Generated by Django 4.2.4 on 2023-09-03 22:52

import applications.metas.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizaciones', '0005_alter_organizacion_industria'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(validators=[applications.metas.models.validate_year_range])),
                ('meta', models.ForeignKey(db_column='fk_meta_x_organizaciones', on_delete=django.db.models.deletion.CASCADE, to='organizaciones.organizacion')),
            ],
        ),
    ]
