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

3. Run `python manage.py migrate` to create the petition models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage a petition (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/petition/ to participate in the petition.

Settings
-----------

There is some settings to set by django-constance (or settings.py):

```python

CONSTANCE_CONFIG = {
    'AGGREMENT_TEXT': ("I accept", 'Text of aggrement in submission form of "ankieta"'),  # Required
    "NEWSLETTER_TEXT": ("I want sign to newsletter"),  # Required
    'NEWSLETTER_DEFAULT': (True, "Set default checked or not for newsletter aggrement"),  # Required
    'ISSUE_SPOT': ("<p>Lorem ipsum</p>", "HTML code of video about petition"),  # Default template
    'ISSUE_DESCRIPTION': ("<p>Lorem ipsum</p>", "HTML code of description of petition"),  # Default template
    'LETTER_TEXT': ("<p><b>To:</b>Lorem</p><p>ipsum</p>", "HTML code of letter with recipient"),  # Default template
    'LETTER_THANK_YOU': ("<p>Lorem ipsum</p>", "HTML code of thank you text"),  # Default template
}
```
