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

        self.local_fields = []

        self.backwards_fk_fields = []
        self.backwards_m2m_fields = []

        self.all_fk_fields = []
        self.all_m2m_fields = []

        self._setup_local_fields()
        self._setup_backwards_fields()

    def _setup_local_fields(self):
        for field in self.opts.local_fields + self.opts.many_to_many:
            name = field.name
            if isinstance(field, models.ForeignKey):
                self.fk_fields.append(name)
                self.all_fk_fields.append(name)
            elif isinstance(field, models.ManyToManyField):
                self.m2m_fields.append(name)
                self.all_m2m_fields.append(name)
            else:
                self.fields.append(name)
            self.local_fields.append(name)

    def _setup_backwards_fields(self):
        for related in self.opts.get_all_related_objects() + self.opts.get_all_related_many_to_many_objects():
            name = related.get_accessor_name()
            field = related.field
            if hasattr(field, "m2m_field_name"):
                self.backwards_m2m_fields.append(name)
                self.all_m2m_fields.append(name)
            else:
                self.backwards_fk_fields.append(name)
                self.all_fk_fields.append(name)
