================================
Cuban Localization (``l10n_cu``)
================================

``l10n_cu`` is a Django app for adapting a product for a cuban market, with Provinces, Municipalities and Zip Codes.

-------
Install
-------
    ``pip install django-l10n-cu``

-----------
Quick start
-----------
1. Add ``"l10n_cu"`` to your INSTALLED_APPS setting like this

    ``INSTALLED_APPS = [``
    ``...,``
    ``'l10n_cu',``
    ``]``

2. Run ``python manage.py migrate`` to create the ``l10n_cu`` models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to view the models populated (you'll need the Admin app enabled).

---------------
Future Features
---------------
* Small towns and other cities in municipalities.
* `urls.py` file