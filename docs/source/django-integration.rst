Django Integration
==================

Installation and Configuration
------------------------------

To configure :code:`loc_authorities` for usage with Django, you must install :code:`loc_authorities` with the optional Django dependencies.

Install into a virtual environment with pip:

.. code-block:: console

    (.venv) $ pip install loc-authorities[django]

Alternatively, install with uv:

.. code-block:: console

    $ uv add loc-authorities --group django

To use :code:`loc_authorities` with Django, you must add :code:`loc_authorities` and its dependencies from :code:`django-autocomplete-light` to the installed applications in your project's :code:`settings.py` file. If you intend to use this in the Django admin interface, it must be added before :code:`django.contrib.admin`:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'dal',
        'dal_alight',
        'loc_authorities',
        ...
    ]

Include the :code`loc-authorities` URLs at the preferred base URL:

.. code-block:: python

    urlpatterns = [
        ...
        path(r'loc-authorities/', include('loc_authorities.urls', namespace='loc-authorities')),
        ...
    ]

---------------------
Use in standard forms
---------------------

To use :code:`loc_authorities` in a standard form, use the provided :code:`LocField` on your form:

.. code-block:: python

    from django import forms
    from loc_authorities.forms import LocField
    
    class MyForm(forms.ModelForm):
        uri = LocField()
    
        class Meta:
            model = MyModel
            fields = ('title', 'uri')

By default, the provided field will query the url :code:`loc-authorities:suggest`. If you have configured your URLs differently or if you want to query a different service, you need to explicitly pass that URL to the widget:

.. code-block:: python

    from django import forms
    from loc_authorities.forms import LocField, LocWidget

    class MyForm(forms.ModelForm):
        uri = LocField(
            widget=LocWidget(url='loc-authorities:subject-search'),
        )

        class Meta:
            model = MyModel
            fields = ('title', 'uri')

Then in the template, it is necessary to include :code:`{{ form.media }}` to load the required JavaScript:

.. code-block:: django

    {% extends 'base-html' %}
    {% load static %}

    {% block content %}
      <form action="" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
      </form>
      {{ form.media }}
    {% endblock %}

-----------------------
Use in the Django Admin
-----------------------

To use :code:`loc_authorities` in the Django admin, create a custom form as described above and then register it in the admin.

.. code-block:: python

    from django.contrib import admin

    from .models import MyModel
    from .forms import MyForm


    class MyModelAdmin(admin.ModelAdmin):
        form = MyForm

    admin.site.register(MyModel, MyModelAdmin)


