import re
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def cubanCIValidator(ci):
    ci = str(ci)
    if not re.match(r"^[0-9]{11}$", ci):
        raise ValidationError(
            _('El CI debe tener 11 dígitos'),
            code='ci_invalid'
        )
    else:
        year = ci[0:1]
        mes = int(ci[2:4])
        dia = int(ci[5:6])
        actual_year = datetime.now().year
        string_year = str(actual_year)
        prefijo = string_year[len(string_year) - 2: len(string_year)]
        year_final = int(prefijo + str(year))
        if year_final >= actual_year:
            prefijo = str(int(prefijo) - 1)
            year_final = int(prefijo + str(year))
        try:
            fecha = datetime(year_final, mes, dia)
        except Exception as e:
            raise ValidationError(
                _('El CI no corresponde con un número válido: ' + str(e)),
                code='ci_invalid'
            )
