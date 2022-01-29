from django.db import migrations
from l10n_cuba.data.provincias import PROVINCIAS


def populate(apps, schema_editor):
    Provincia = apps.get_model('l10n_cuba', 'Provincia')

    for provincia in PROVINCIAS:
        prov = Provincia.objects.create(name=provincia['name'], short_name=provincia['short_name'])
        prov.save()


def reverse_populate(apps, schema_editor):
    Provincia = apps.get_model('l10n_cuba', 'Provincia')
    provincias = Provincia.objects.all()
    provincias.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('l10n_cuba', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate, reverse_populate)
    ]
