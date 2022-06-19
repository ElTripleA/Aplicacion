from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class RegistroCovidResource(resources.ModelResource):
    class Meta:
        model = RegistroCovid


class RegistroCovidAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ID_de_caso', 'id']
    list_display = ('id', 'Fecha_reporte_web', 'ID_de_caso', 'Edad', 'Estado')
    resource_class = RegistroCovidResource


class InfoAutoresAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombre_autor']
    list_display = ('id', 'Nombre_autor', 'Descripcion_autor', 'Universidad_autor')


admin.site.register(RegistroCovid, RegistroCovidAdmin)
admin.site.register(InfoAutores, InfoAutoresAdmin)