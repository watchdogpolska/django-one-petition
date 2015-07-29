=====
Django-one-petition
=====

Django-one-petition is a simple Django app to conduct Web-based petition. We provide maps of signatures.


Quick start
-----------

1. Add "petition" and "import_export" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
	'import_export',
        'petition',
    ]

2. Include the petition URLconf in your project urls.py like this::

    url(r'^petition/', include('petition.urls')),

3. Run `python manage.py migrate` to create the database tables.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage a petition (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/petition/ to participate in the petition.
