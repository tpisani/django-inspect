django-inspect
==============

Provides information about `django <https://www.djangoproject.com/>`_ models by
a series of conveniences, such as its fields (local, foreign keys, many to many).
Its only requirement is any version of django.

Here is a resume of what **django-inspect** offers:

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


Installation
------------

**django-inspect** is available through **pip**:

::

    pip install django-inspect


Usage
-----

.. code:: python

    from django.contrib.auth.models import User

    from django_inspect import Inspect

    # passing an instance/object is also possible
    inspect = Inspect(User)

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
