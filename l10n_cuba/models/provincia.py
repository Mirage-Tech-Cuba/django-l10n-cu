from django.db import models
from django.utils.translation import gettext_lazy as _


class Provincia(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=60)
    short_name = models.CharField(verbose_name=_('Short name'), max_length=3, unique=True)

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')

    def __str__(self):
        return self.name
