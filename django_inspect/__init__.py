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

        self.non_rel_fields = []

        self.fk_fields = []
        self.m2m_fields = []

        self.backwards_fk_fields = []
        self.backwards_m2m_fields = []

        self.all_fk_fields = []
        self.all_m2m_fields = []

        self.all_fields = []

        self._setup_local_fields()
        self._setup_backwards_fields()

    def _setup_fields(self, backwards, fields):
        for field in fields:
            if backwards:
                name = field.get_accessor_name()
                field = field.field
            else:
                name = field.name
                self.fields.append(name)
            if isinstance(field, models.ForeignKey):
                if backwards:
                    self.backwards_fk_fields.append(name)
                else:
                    self.fk_fields.append(name)
                self.all_fk_fields.append(name)
            elif isinstance(field, models.ManyToManyField):
                if backwards:
                    self.backwards_m2m_fields.append(name)
                else:
                    self.m2m_fields.append(name)
                self.all_m2m_fields.append(name)
            else:
                self.non_rel_fields.append(name)
            self.all_fields.append(name)

    def _setup_local_fields(self):
        self._setup_fields(False, self.opts.local_fields
                                + self.opts.many_to_many)

    def _setup_backwards_fields(self):
        self._setup_fields(True, self.opts.get_all_related_objects()
                               + self.opts.get_all_related_many_to_many_objects())
