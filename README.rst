==============
django-inspect
==============

.. image:: https://api.travis-ci.org/tpisani/django-inspect.svg

Provides inspection conveniences for `django <https://www.djangoproject.com/>`_ models.


Features
========

Convenience attributes
----------------------

all_fields
    All model fields, including all relationships (back and forth).

fields
    Only local fields, ie. any regular field and relationships (excluding backwards).

non_rel_fields
    Basically the same thing as **fields**, but excluding all relationships.

fk_fields
    Local foreign key fields.

backwards_fk_fields
    Only backwards foreign key fields.

all_fk_fields
    All foreign key fields (back and forth).

m2m_fields
    Local many to many fields.

backwards_m2m_fields
    Only backwards many to many fields.

all_m2m_fields
    All many to many fields (back and forth).


Sub-inspecting
--------------

Futher inspection on relationship fields.

After inspecting a model (creating an ``Inspect`` instance) call:

``inspect.sub_inspect("field")``

*Paths are supported too:*

``inspect.sub_inspect("field.other_field..")``

It returns a new ``Inspect`` instance, containing information about
the target model of the relationship field.


Installation
============

Available through **pip**:

::

    $ pip install django-inspect


Usage
=====

Simple inspection
-----------------

.. code:: python

    from django.contrib.auth.models import User

    from django_inspect import Inspect

    inspect = Inspect(User)
    
    # Using an instance/object is also possible.
    # user = User()
    # inspect = Inspect(user)

    inspect.fields
    [u'id', 'password', 'last_login', 'is_superuser', 'username',
     'first_name', 'last_name', 'email', 'is_staff', 'is_active',
     'date_joined', 'groups', 'user_permissions']

    inspect.non_rel_fields
    [u'id', 'password', 'last_login', 'is_superuser', 'username',
     'first_name', 'last_name', 'email', 'is_staff', 'is_active',
     'date_joined']

    inspect.m2m_fields
    ['groups', 'user_permissions']

    inspect.backwards_fk_fields
    ['logentry_set']


Sub-inspecting
--------------

.. code:: python

    from django.contrib.auth.models import User

    from django_inspect import Inspect

    inspect = Inspect(User)

    sub_inspect = inspect.sub_inspect("user_permissions")

    sub_inspect.all_fields
    [u'id', 'name', 'content_type', 'codename']

    futher_inspect = sub_inspect.sub_inspect("content_type")
    futher_inspect.all_fields
    [u'id', 'name', 'app_label', 'model']

    # Sub-inspecting by path

    sub_inspect = inspect.sub_inspect("user_permissions.content_type")

    sub_inspect.all_fields
    [u'id', 'name', 'app_label', 'model']


Testing
=======


Install
-------

Run ``make install`` to install dev requirements.


Run tests
---------

Run ``make test`` to run tests.
