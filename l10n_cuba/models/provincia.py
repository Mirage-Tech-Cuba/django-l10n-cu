from django.db import models
from django.utils.translation import gettext_lazy as _


class Provincia(models.Model):
    nombre = models.CharField(verbose_name='Nombre', primary_key=True, max_length=60)
    nombre_corto = models.CharField(verbose_name=_('Nombre Corto'), max_length=3, unique=True)

    class Meta:
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')

    def __str__(self):
        return self.nombre
