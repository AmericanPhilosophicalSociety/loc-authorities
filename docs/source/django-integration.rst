Django Integration
==================

Installation and Configuration
------------------------------

To configure loc-authorities for usage with Django, you must install loc-authorities with the optional Django dependencies.

Install into a virtual environment with pip:

.. code-block:: console

    (.venv) $ pip install loc-authorities[django]

Alternatively, install with uv:

.. code-block:: console

    $ uv add loc-authorities --group django

To use loc-authorities with Django, you must add loc-authorities and its dependencies from django-autocomplete-light to the installed applications in your project's settings.py file. If you intend to use this in the Django admin interface, it must be added before django.contrib.admin:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'dal',
        'dal_alight',
        'loc_authorities',
        ...
    ]

Include the loc-authorities urls at the preferred base url:

.. code-block:: python

    urlpatterns = [
        ...
        path(r'loc-authorities/', include('loc_authorities.urls', namespace='loc_authorities')),
        ...
    ]
