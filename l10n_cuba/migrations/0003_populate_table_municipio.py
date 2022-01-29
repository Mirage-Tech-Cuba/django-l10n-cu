import sys
from django.db import migrations, transaction
from l10n_cuba.data.municipios import get_provincia


def populate(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    Municipio = apps.get_model('l10n_cuba', 'Municipio')
    p = get_provincia(apps=apps)
    MUNICIPIOS = [
        # Pinar del Rio
        {'name': 'Sandino', 'state': p['pr']},
        {'name': 'Mantua', 'state': p['pr']},
        {'name': 'Minas de Matahambre', 'state': p['pr']},
        {'name': 'Viñales', 'state': p['pr']},
        {'name': 'La Palma', 'state': p['pr']},
        {'name': 'Los Palacios', 'state': p['pr']},
        {'name': 'Consolación del Sur', 'state': p['pr']},
        {'name': 'Pinar del Río', 'state': p['pr']},
        {'name': 'San Luis', 'state': p['pr']},
        {'name': 'San Juan y Martínez', 'state': p['pr']},
        {'name': 'Guane', 'state': p['pr']},

        # Artemisa
        {'name': 'Bahía Honda', 'state': p['art']},
        {'name': 'Mariel', 'state': p['art']},
        {'name': 'Guanajay', 'state': p['art']},
        {'name': 'Caimito', 'state': p['art']},
        {'name': 'Bauta', 'state': p['art']},
        {'name': 'San Antonio de los Baños', 'state': p['art']},
        {'name': 'Güira de Melena', 'state': p['art']},
        {'name': 'Alquízar', 'state': p['art']},
        {'name': 'Artemisa', 'state': p['art']},
        {'name': 'Candelaria', 'state': p['art']},
        {'name': 'San Cristóbal', 'state': p['art']},

        # La Habana
        {'name': 'Playa', 'state': p['lh']},
        {'name': 'Plaza de la Revolución', 'state': p['lh']},
        {'name': 'Centro Habana', 'state': p['lh']},
        {'name': 'La Habana Vieja', 'state': p['lh']},
        {'name': 'Regla', 'state': p['lh']},
        {'name': 'La Habana del Este', 'state': p['lh']},
        {'name': 'Guanabacoa', 'state': p['lh']},
        {'name': 'San Miguel del Padrón', 'state': p['lh']},
        {'name': 'Diez de Octubre', 'state': p['lh']},
        {'name': 'Cerro', 'state': p['lh']},
        {'name': 'Marianao', 'state': p['lh']},
        {'name': 'La Lisa', 'state': p['lh']},
        {'name': 'Boyeros', 'state': p['lh']},
        {'name': 'Arroyo Naranjo', 'state': p['lh']},
        {'name': 'Cotorro', 'state': p['lh']},

        # Mayabeque
        {'name': 'Bejucal', 'state': p['may']},
        {'name': 'San José de las Lajas', 'state': p['may']},
        {'name': 'Jaruco', 'state': p['may']},
        {'name': 'Santa Cruz del Norte', 'state': p['may']},
        {'name': 'Madruga', 'state': p['may']},
        {'name': 'Nueva Paz', 'state': p['may']},
        {'name': 'San Nicolás', 'state': p['may']},
        {'name': 'Güines', 'state': p['may']},
        {'name': 'Batabanó', 'state': p['may']},
        {'name': 'Quivicán', 'state': p['may']},
        {'name': 'Melena del Sur', 'state': p['may']},

        # Matanzas
        {'name': 'Matanzas', 'state': p['mtz']},
        {'name': 'Cárdenas', 'state': p['mtz']},
        {'name': 'Martí', 'state': p['mtz']},
        {'name': 'Colón', 'state': p['mtz']},
        {'name': 'Perico', 'state': p['mtz']},
        {'name': 'Jovellanos', 'state': p['mtz']},
        {'name': 'Pedro Betancourt', 'state': p['mtz']},
        {'name': 'Limonar', 'state': p['mtz']},
        {'name': 'Unión de Reyes', 'state': p['mtz']},
        {'name': 'Ciénaga de Zapata', 'state': p['mtz']},
        {'name': 'Jagüey Grande', 'state': p['mtz']},
        {'name': 'Calimete', 'state': p['mtz']},
        {'name': 'Los Arabos', 'state': p['mtz']},

        # Villa Clara
        {'name': 'Corralillo', 'state': p['vcl']},
        {'name': 'Quemado de Güines', 'state': p['vcl']},
        {'name': 'Sagua la Grande', 'state': p['vcl']},
        {'name': 'Encrucijada', 'state': p['vcl']},
        {'name': 'Camajuaní', 'state': p['vcl']},
        {'name': 'Caibarién', 'state': p['vcl']},
        {'name': 'Remedios', 'state': p['vcl']},
        {'name': 'Placetas', 'state': p['vcl']},
        {'name': 'Santa Clara', 'state': p['vcl']},
        {'name': 'Cifuentes', 'state': p['vcl']},
        {'name': 'Santo Domingo', 'state': p['vcl']},
        {'name': 'Ranchuelo', 'state': p['vcl']},
        {'name': 'Manicaragua', 'state': p['vcl']},

        # Cienfuegos
        {'name': 'Abreus', 'state': p['cfg']},
        {'name': 'Aguada de Pasajeros', 'state': p['cfg']},
        {'name': 'Cienfuegos', 'state': p['cfg']},
        {'name': 'Cruces', 'state': p['cfg']},
        {'name': 'Cumanayagua', 'state': p['cfg']},
        {'name': 'Lajas', 'state': p['cfg']},
        {'name': 'Palmira', 'state': p['cfg']},
        {'name': 'Rodas', 'state': p['cfg']},

        # Sancti Spiritus
        {'name': 'Yaguajay', 'state': p['ssp']},
        {'name': 'Jatibonico', 'state': p['ssp']},
        {'name': 'Taguasco', 'state': p['ssp']},
        {'name': 'Cabaiguán', 'state': p['ssp']},
        {'name': 'Fomento', 'state': p['ssp']},
        {'name': 'Trinidad', 'state': p['ssp']},
        {'name': 'Sancti Spíritus', 'state': p['ssp']},
        {'name': 'La Sierpe', 'state': p['ssp']},

        # Ciego de Avila
        {'name': 'Chambas', 'state': p['cav']},
        {'name': 'Morón', 'state': p['cav']},
        {'name': 'Bolivia', 'state': p['cav']},
        {'name': 'Primero de Enero', 'state': p['cav']},
        {'name': 'Ciro Redondo', 'state': p['cav']},
        {'name': 'Florencia', 'state': p['cav']},
        {'name': 'Majagua', 'state': p['cav']},
        {'name': 'Ciego de Ávila', 'state': p['cav']},
        {'name': 'Venezuela', 'state': p['cav']},
        {'name': 'Baraguá', 'state': p['cav']},

        # Camaguey
        {'name': 'Carlos Manuel de Céspedes', 'state': p['cmg']},
        {'name': 'Esmeralda', 'state': p['cmg']},
        {'name': 'Sierra de Cubitas', 'state': p['cmg']},
        {'name': 'Minas', 'state': p['cmg']},
        {'name': 'Nuevitas', 'state': p['cmg']},
        {'name': 'Sibanicú', 'state': p['cmg']},
        {'name': 'Florida', 'state': p['cmg']},
        {'name': 'Camagüey', 'state': p['cmg']},
        {'name': 'Vertientes', 'state': p['cmg']},
        {'name': 'Jimaguayú', 'state': p['cmg']},
        {'name': 'Santa Cruz del Sur', 'state': p['cmg']},
        {'name': 'Guáimaro', 'state': p['cmg']},
        {'name': 'Najasa', 'state': p['cmg']},

        # Las Tunas
        {'name': 'Manatí', 'state': p['ltu']},
        {'name': 'Puerto Padre', 'state': p['ltu']},
        {'name': 'Jesús Menéndez', 'state': p['ltu']},
        {'name': 'Majibacoa', 'state': p['ltu']},
        {'name': 'Las Tunas', 'state': p['ltu']},
        {'name': 'Jobabo', 'state': p['ltu']},
        {'name': 'Colombia', 'state': p['ltu']},
        {'name': 'Amancio', 'state': p['ltu']},

        # Holguin
        {'name': 'Gibara', 'state': p['hlg']},
        {'name': 'Rafael Freyre', 'state': p['hlg']},
        {'name': 'Banes', 'state': p['hlg']},
        {'name': 'Antilla', 'state': p['hlg']},
        {'name': 'Báguanos', 'state': p['hlg']},
        {'name': 'Holguín', 'state': p['hlg']},
        {'name': 'Calixto García', 'state': p['hlg']},
        {'name': 'Cacocum', 'state': p['hlg']},
        {'name': 'Urbano Noris', 'state': p['hlg']},
        {'name': 'Cueto', 'state': p['hlg']},
        {'name': 'Mayarí', 'state': p['hlg']},
        {'name': 'Frank País', 'state': p['hlg']},
        {'name': 'Sagua de Tánamo', 'state': p['hlg']},
        {'name': 'Moa', 'state': p['hlg']},

        # Granma
        {'name': 'Río Cauto', 'state': p['grm']},
        {'name': 'Cauto Cristo', 'state': p['grm']},
        {'name': 'Jiguaní', 'state': p['grm']},
        {'name': 'Bayamo', 'state': p['grm']},
        {'name': 'Yara', 'state': p['grm']},
        {'name': 'Manzanillo', 'state': p['grm']},
        {'name': 'Campechuela', 'state': p['grm']},
        {'name': 'Media Luna', 'state': p['grm']},
        {'name': 'Niquero', 'state': p['grm']},
        {'name': 'Pilón', 'state': p['grm']},
        {'name': 'Bartolomé Masó', 'state': p['grm']},
        {'name': 'Buey Arriba', 'state': p['grm']},
        {'name': 'Guisa', 'state': p['grm']},

        # Santiago de Cuba
        {'name': 'Contramaestre', 'state': p['scu']},
        {'name': 'Mella', 'state': p['scu']},
        {'name': 'San Luis', 'state': p['scu']},
        {'name': 'Segundo Frente', 'state': p['scu']},
        {'name': 'Songo - La Maya', 'state': p['scu']},
        {'name': 'Santiago de Cuba', 'state': p['scu']},
        {'name': 'Palma Soriano', 'state': p['scu']},
        {'name': 'Tercer Frente', 'state': p['scu']},
        {'name': 'Guamá', 'state': p['scu']},

        # Guantanamo
        {'name': 'El Salvador', 'state': p['gtm']},
        {'name': 'Manuel Tames', 'state': p['gtm']},
        {'name': 'Yateras', 'state': p['gtm']},
        {'name': 'Baracoa', 'state': p['gtm']},
        {'name': 'Maisí', 'state': p['gtm']},
        {'name': 'Imías', 'state': p['gtm']},
        {'name': 'San Antonio del Sur', 'state': p['gtm']},
        {'name': 'Caimanera', 'state': p['gtm']},
        {'name': 'Guantánamo', 'state': p['gtm']},
        {'name': 'Niceto Pérez', 'state': p['gtm']},

        # Isla de la Juventud
        {'name': 'Isla de la Juventud', 'state': p['isj']},
    ]
    with transaction.atomic():
        for municipio in MUNICIPIOS:
            mun = Municipio.objects.create(name=municipio['name'], state=municipio['state'])
            mun.save()


def reverse_populate(apps, schema_editor):
    Municipio = apps.get_model('l10n_cuba', 'Municipio')
    municipios = Municipio.objects.all()
    municipios.delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('l10n_cuba', '0002_populate_table_provincia'),
    ]

    operations = [
        migrations.RunPython(populate, reverse_populate)
    ]
