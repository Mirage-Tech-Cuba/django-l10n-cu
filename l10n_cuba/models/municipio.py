from django.db import models
from django.utils.translation import gettext_lazy as _

from .provincia import Provincia


class Municipio(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    state = models.ForeignKey(to=Provincia, on_delete=models.PROTECT, related_name='municipalities')

    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')

    def __str__(self):
        return self.name
