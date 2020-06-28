from django.contrib import admin
from .models import Provincia, Municipio

# Register your models here.
admin.site.register(Provincia)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_filter = ['provincia']
