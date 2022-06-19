# Generated by Django 3.2.13 on 2022-06-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCovid',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Fecha_reporte_web', models.DateTimeField(null=True, verbose_name='fecha reporte web')),
                ('ID_de_caso', models.IntegerField(verbose_name='ID de caso')),
                ('Fecha_de_noti', models.DateTimeField(null=True, verbose_name='Fecha de notificación')),
                ('DAVIPOLA_departamento', models.IntegerField(null=True, verbose_name='Código DIVIPOLA departamento')),
                ('Nombre_departamento', models.CharField(max_length=100, null=True, verbose_name='Nombre departamento')),
                ('DAVIPOLA_municipio', models.IntegerField(null=True, verbose_name='Código DIVIPOLA municipio')),
                ('Nombre_Municipio', models.CharField(max_length=100, null=True, verbose_name='Nombre municipio')),
                ('Edad', models.IntegerField(null=True, verbose_name='Edad')),
                ('Unidad_de_edad', models.IntegerField(null=True, verbose_name='Unidad de medida de edad')),
                ('Sexo', models.CharField(max_length=20, null=True, verbose_name='Sexo')),
                ('Tipo_de_contagio', models.CharField(max_length=100, null=True, verbose_name='Tipo de contagio')),
                ('Ubicacion_del_caso', models.CharField(max_length=100, null=True, verbose_name='Ubicación del caso')),
                ('Estado', models.CharField(max_length=100, null=True, verbose_name='Estado')),
                ('Codigo_ISO_del_pais', models.IntegerField(blank=True, null=True, verbose_name='Código ISO del país')),
                ('Nombre_del_pais', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del país')),
                ('Recuperado', models.CharField(max_length=100, null=True, verbose_name='Recuperado')),
                ('Fecha_sintomas', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inicio de síntomas')),
                ('Fecha_muerte', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de muerte')),
                ('Fecha_diagnostico', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de diagnóstico')),
                ('Fecha_recuperacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de recuperación')),
                ('Tiempo_recuperacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo de recuperación')),
                ('Pertenencia_etnica', models.IntegerField(null=True, verbose_name='Pertenencia étnica')),
                ('Nombre_etnia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del grupo étnico')),
            ],
            options={
                'verbose_name': 'Registro de caso',
                'verbose_name_plural': 'Registro de los casos',
            },
        ),
    ]