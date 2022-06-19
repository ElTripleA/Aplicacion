from django.db import models

# Create your models here.


class RegistroCovid(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Fecha_reporte_web = models.DateTimeField("fecha reporte web", auto_now=False, auto_now_add=False, null=True, blank=False)
    ID_de_caso = models.IntegerField("ID de caso", null=False, blank=False)
    Fecha_de_noti = models.DateTimeField("Fecha de notificación", auto_now=False, auto_now_add=False, null=True, blank=False)
    DAVIPOLA_departamento = models.IntegerField("Código DIVIPOLA departamento", null=True, blank=False)
    Nombre_departamento = models.CharField("Nombre departamento", max_length=100, null=True, blank=False)
    DAVIPOLA_municipio = models.IntegerField("Código DIVIPOLA municipio", null=True, blank=False)
    Nombre_Municipio = models.CharField("Nombre municipio", max_length=100, null=True, blank=False)
    Edad = models.IntegerField("Edad", null=True, blank=False)
    Unidad_de_edad = models.IntegerField("Unidad de medida de edad", null=True, blank=False)
    Sexo = models.CharField("Sexo", max_length=20, null=True, blank=False)
    Tipo_de_contagio = models.CharField("Tipo de contagio", max_length=100, null=True, blank=False)
    Ubicacion_del_caso = models.CharField("Ubicación del caso", max_length=100, null=True, blank=False)
    Estado = models.CharField("Estado", max_length=100, null=True, blank=False)
    Codigo_ISO_del_pais = models.IntegerField("Código ISO del país", null=True, blank=True)
    Nombre_del_pais = models.CharField("Nombre del país", max_length=100, null=True, blank=True)
    Recuperado = models.CharField("Recuperado", max_length=100, null=True, blank=False)
    Fecha_sintomas = models.DateTimeField("Fecha de inicio de síntomas", auto_now=False, auto_now_add=False, null=True,blank=True)
    Fecha_muerte = models.DateTimeField("Fecha de muerte", auto_now=False, auto_now_add=False, null=True, blank=True)
    Fecha_diagnostico = models.DateTimeField("Fecha de diagnóstico", auto_now=False, auto_now_add=False, null=True, blank=True)
    Fecha_recuperacion = models.DateTimeField("Fecha de recuperación", auto_now=False, auto_now_add=False, null=True, blank=True)
    Tiempo_recuperacion = models.CharField("Tipo de recuperación", max_length=100, null=True, blank=True)
    Pertenencia_etnica = models.IntegerField("Pertenencia étnica", null=True, blank=False)
    Nombre_etnia = models.CharField("Nombre del grupo étnico", max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = "Registro de caso"
        verbose_name_plural = "Registro de los casos"

    def __int__(self):
        return self.ID_de_caso


class InfoAutores(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Nombre_autor = models.CharField("Nombre del autor", max_length=100, null=True, blank=False)
    Descripcion_autor = models.CharField("Descripción del autor", max_length=200, null=True, blank=False)
    Universidad_autor = models.CharField("Universidad autor", max_length=200, null=True, blank=False)
    Contacto_autor = models.CharField("Contacto autor", max_length=200, null=True, blank=False)

    class Meta:
        verbose_name = "Información de autor"
        verbose_name_plural = "Información de autores"
