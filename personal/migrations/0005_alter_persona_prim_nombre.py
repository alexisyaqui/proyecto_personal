# Generated by Django 4.0.4 on 2022-05-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_persona_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='prim_nombre',
            field=models.CharField(max_length=50, verbose_name='Primer Nombre'),
        ),
    ]
