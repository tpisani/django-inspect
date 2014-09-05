#!/usr/bin/env python

import sys

from os.path import dirname, abspath

from django.conf import settings

from nose.plugins.plugintest import run_buffered as run


if not settings.configured:
    settings.configure(
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "django-inspect.db",
            }
        },
        DEBUG=False,
        SITE_ID=1,
    )

if __name__ == "__main__":
    run(argv=sys.argv)
