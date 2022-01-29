from django.conf import settings
from django.contrib import admin

L10N_CUBA_ADMIN = getattr(settings, "L10N_CUBA_ADMIN", False)

if L10N_CUBA_ADMIN:
    from .models import Provincia, Municipio, CodigoPostal


    @admin.register(Provincia)
    class ProvinciaAdmin(admin.ModelAdmin):
        list_display = ['name', 'short_name', ]


    @admin.register(Municipio)
    class MunicipioAdmin(admin.ModelAdmin):
        list_filter = ['state']
        list_display = ('state', 'name', 'zip_codes')

        def zip_codes(self, obj):
            return ', '.join(str(zip_code.full_value) for zip_code in obj.zip_codes.all())


    @admin.register(CodigoPostal)
    class CodigoPostalAdmin(admin.ModelAdmin):
        list_filter = ['municipality__state']
        list_display = ('state', 'municipality', 'zip_code', 'place')
        ordering = ['municipio', 'codigo_postal']

        def state(self, obj):
            return obj.municipality.state
