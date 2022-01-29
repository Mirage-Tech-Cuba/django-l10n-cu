from django.core.exceptions import ObjectDoesNotExist


def get_provincia(apps):
    try:
        p = dict()
        Provincia = apps.get_model('l10n_cuba', 'Provincia')

        p['pr'] = Provincia.objects.get(short_name='PR')
        p['art'] = Provincia.objects.get(short_name='ART')
        p['lh'] = Provincia.objects.get(short_name='LH')
        p['may'] = Provincia.objects.get(short_name='MAY')
        p['mtz'] = Provincia.objects.get(short_name='MTZ')
        p['vcl'] = Provincia.objects.get(short_name='VCL')
        p['cfg'] = Provincia.objects.get(short_name='CFG')
        p['ssp'] = Provincia.objects.get(short_name='SSP')
        p['cav'] = Provincia.objects.get(short_name='CAV')
        p['cmg'] = Provincia.objects.get(short_name='CMG')
        p['ltu'] = Provincia.objects.get(short_name='LTU')
        p['grm'] = Provincia.objects.get(short_name='GRM')
        p['hlg'] = Provincia.objects.get(short_name='HLG')
        p['scu'] = Provincia.objects.get(short_name='SCU')
        p['gtm'] = Provincia.objects.get(short_name='GTM')
        p['isj'] = Provincia.objects.get(short_name='ISJ')
        return p
    except ObjectDoesNotExist:
        print('Object not found.')
    except:
        print('Error running migration.')
