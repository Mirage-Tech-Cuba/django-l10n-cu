# from l10n_cuba.models import Provincia
from django.core.exceptions import ObjectDoesNotExist


def get_provincia(apps):
    try:
        p = dict()
        Provincia = apps.get_model('l10n_cuba', 'Provincia')

        p['pr'] = Provincia.objects.get(nombre_corto='PR')
        p['art'] = Provincia.objects.get(nombre_corto='ART')
        p['lh'] = Provincia.objects.get(nombre_corto='LH')
        p['may'] = Provincia.objects.get(nombre_corto='MAY')
        p['mtz'] = Provincia.objects.get(nombre_corto='MTZ')
        p['vcl'] = Provincia.objects.get(nombre_corto='VCL')
        p['cfg'] = Provincia.objects.get(nombre_corto='CFG')
        p['ssp'] = Provincia.objects.get(nombre_corto='SSP')
        p['cav'] = Provincia.objects.get(nombre_corto='CAV')
        p['cmg'] = Provincia.objects.get(nombre_corto='CMG')
        p['ltu'] = Provincia.objects.get(nombre_corto='LTU')
        p['grm'] = Provincia.objects.get(nombre_corto='GRM')
        p['hlg'] = Provincia.objects.get(nombre_corto='HLG')
        p['scu'] = Provincia.objects.get(nombre_corto='SCU')
        p['gtm'] = Provincia.objects.get(nombre_corto='GTM')
        p['isj'] = Provincia.objects.get(nombre_corto='ISJ')
        return p
    except ObjectDoesNotExist:
        print(f'Ese nombre no se encuentra en ninguna provincia.')
    except:
        print(f'Ocurrio un error al correr la migration')
