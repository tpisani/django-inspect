import inspect

from django.db import models


class Inspect(object):

    def __init__(self, model):
        if not inspect.isclass(model):
            model = model.__class__
        if not models.Model in model.mro():
            raise TypeError("{} is not a django model".format(model.__name__))

        self.model = model
        self.opts = model._meta
        self.fields = []
        self.fk_fields = []
        self.m2m_fields = []

        self._setup_fields()
        self._setup_rel_fields()

    def _setup_fields(self):
        for field in self.opts.local_fields:
            self.fields.append(field.name)

    def _setup_rel_fields(self):
        for name in self.opts.get_all_field_names():
            field, model, direct, m2m = self.opts.get_field_by_name(name)
            if not direct:
                name = field.get_accessor_name()
                field = field.field
            if not field.rel:
                continue
            if m2m:
                self.m2m_fields.append(name)
            else:
                self.fk_fields.append(name)
