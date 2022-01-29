
def get_municipio(apps):
    try:
        p = dict()
        Municipio = apps.get_model('l10n_cuba', 'Municipio')

        for municipio in Municipio.objects.all():
            p[municipio.name] = municipio
        return p
    except:
        print('Error running migration.')
