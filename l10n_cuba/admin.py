from django.conf import settings
from django.contrib import admin

L10N_CUBA_ADMIN = getattr(settings, "L10N_CUBA_ADMIN", False)

if L10N_CUBA_ADMIN:

    from .models import Provincia, Municipio, CodigoPostal

    # Register your models here.
    admin.site.register(Provincia)

    @admin.register(Municipio)
    class MunicipioAdmin(admin.ModelAdmin):
        list_filter = ['provincia']
        list_display = ('provincia', 'nombre', 'codigos')
        empty_value_display = '---'

        def codigos(self, obj):
            return ' - '.join(str(codigo.full_value) for codigo in obj.codigos_postales.all())

    @admin.register(CodigoPostal)
    class CodigoPostalAdmin(admin.ModelAdmin):
        list_filter = ['municipio__provincia']
        list_display = ('provincia', 'municipio', 'codigo_postal', 'localidad')
        ordering = ['municipio', 'codigo_postal']
        empty_value_display = '---'

        def provincia(self, obj):
            return obj.municipio.provincia
