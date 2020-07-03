from django.db import models
from .provincia import Provincia
from django.utils.translation import gettext_lazy as _


class Municipio(models.Model):
    # nombre = models.CharField(verbose_name=_('Nombre'), primary_key=True, max_length=50)
    nombre = models.CharField(verbose_name=_('Nombre'), max_length=50)
    provincia = models.ForeignKey(to=Provincia, on_delete=models.PROTECT, related_name='municipios')

    class Meta:
        verbose_name = _('Municipio')
        verbose_name_plural = _('Municipios')

    def __str__(self):
        return self.nombre
