# Generated by Django 3.2.8 on 2021-10-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='Solicitud',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Tiempo_atencion',
            field=models.IntegerField(),
        ),
    ]
