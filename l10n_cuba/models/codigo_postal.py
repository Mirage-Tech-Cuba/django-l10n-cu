from django.db import models

from .municipio import Municipio
from django.utils.translation import gettext_lazy as _


class CodigoPostal(models.Model):
    codigo_postal = models.PositiveIntegerField(verbose_name=_('Código Postal'))
    localidad = models.CharField(verbose_name=_('Localidad'), blank=True, null=True, max_length=150)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='codigos_postales')

    class Meta:
        verbose_name = _('Código Postal')
        verbose_name_plural = _('Códigos Postales')

    def __str__(self):
        return str(self.codigo_postal)

    @property
    def full_value(self):
        if self.localidad is not None and not self.localidad == '':
            return f"{self.codigo_postal} ({self.localidad})"
        return self.codigo_postal
