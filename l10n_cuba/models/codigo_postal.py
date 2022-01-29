from django.db import models

from .municipio import Municipio
from django.utils.translation import gettext_lazy as _


class CodigoPostal(models.Model):
    zip_code = models.PositiveIntegerField(verbose_name=_('ZIP Code'))
    place = models.CharField(verbose_name=_('Town/City/Zone'), blank=True, null=True, max_length=150)
    municipality = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='zip_codes')

    class Meta:
        verbose_name = _('ZIP Code')
        verbose_name_plural = _('ZIP Codes')

    def __str__(self):
        return str(self.zip_code)

    @property
    def full_value(self):
        if self.place is not None and self.place != '':
            return f"{self.zip_code} ({self.place})"
        return self.zip_code
