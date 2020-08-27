==================================
Cuban Localization (``l10n_cuba``)
==================================

``l10n_cuba`` is a Django app for adapting a product for a cuban market, with Provinces, Municipalities and Zip Codes.

-------
Install
-------
    ``pip install django-l10n-cu``

-----------
Quick start
-----------
1. Add ``"l10n_cuba"`` to your INSTALLED_APPS setting like this

    INSTALLED_APPS = [
    ...,
    'l10n_cuba',
    ``]``

2. Run ``python manage.py migrate`` to create the ``l10n_cuba`` models.

3. You need to specify the ``L10N_CUBA_ADMIN`` variable in your settings file, and set it to ``True`` enable the admin for this app.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to view the models populated (you'll need the Admin app enabled).

-----
Usage
-----

Get all Provinces
    >>> from l10n_cuba.models import Provincia
    >>> p = Provincia.objects.all()
    <QuerySet [<Provincia: Pinar del Río>, <Provincia: Artemisa>, <Provincia: La Habana>, <Provincia: Mayabeque>, <Provincia: Matanzas>, <Provincia: Villa Clara>, <Provincia: Cienfuegos>, <Provincia: Sancti Spíritus>, <Provincia: Ciego de Ávila>, <Provincia: Camagüey>, <Provincia: Las Tunas>, <Provincia: Granma>, <Provincia: Holguín>, <Provincia: Santiago de Cuba>, <Provincia: Guantánamo>, <Provincia: Isla de la Juventud>]>


Get all Municipalities in a Province
    >>> from l10n_cuba.models import Provincia
    >>> p = Provincia.objects.get(nombre_corto='MTZ')
    >>> m = p.municipios.all()
    <QuerySet [<Municipio: Matanzas>, <Municipio: Cárdenas>, <Municipio: Martí>, <Municipio: Colón>, <Municipio: Perico>, <Municipio: Jovellanos>, <Municipio: Pedro Betancourt>, <Municipio: Limonar>, <Municipio: Unión de Reyes>, <Municipio: Ciénaga de Zapata>, <Municipio: Jagüey Grande>, <Municipio: Calimete>, <Municipio: Los Arabos>]>

Ask if a Municipality is within a Province
    >>> from l10n_cuba.models import Municipio, Provincia
    >>> cardenas = Municipio.objects.get(nombre='Cárdenas')
    >>> p_mtz = Provincia.objects.get(nombre_corto='MTZ')
    >>> cardenas in p_mtz.municipios.all()
    True

--------
Features
--------
* Validators
    >>> from l10n_cuba.validators import cubanCIValidator
    >>> ci = models.CharField(max_length=11, validators=[cubanCIValidator])

* Custom Fields
    >>> from l10n_cuba.fields import GroupedModelChoiceField
    >>> from l10n_cuba.models import Municipio
    >>> location = GroupedModelChoiceField(queryset=Municipio.objects.all(), choices_groupby='provincia',)

---------------
Future Features
---------------
* Small towns and other cities in municipalities.
* `urls.py` file.
* Django-Rest-Framework integration.
* Methods for comparisons.
* Map snippets for the whole country and provinces only. (help wanted)
