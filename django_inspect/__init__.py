import inspect

from django.db import models


class Inspect(object):
    """
    Provides information about django models by a series of conveniences,
    such as its fields (local, foreign keys, many to many).
    """

    def __init__(self, model):
        if not inspect.isclass(model):
            model = model.__class__
        if models.Model not in model.mro():
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

    def _field_info(self, field):
        return field.name, field

    def _backwards_field_info(self, field):
        return field.get_accessor_name(), field.field

    def _setup_fields(self, backwards, fields):
        if backwards:
            field_info = self._backwards_field_info
            fk_list = self.backwards_fk_fields
            m2m_list = self.backwards_m2m_fields
        else:
            field_info = self._field_info
            fk_list = self.fk_fields
            m2m_list = self.m2m_fields
        for field in fields:
            name, field = field_info(field)
            if not backwards:
                self.fields.append(name)
            if isinstance(field, models.ForeignKey):
                fk_list.append(name)
                self.all_fk_fields.append(name)
            elif isinstance(field, models.ManyToManyField):
                m2m_list.append(name)
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

    def sub_inspect(self, fieldname):
        if fieldname in self.non_rel_fields:
            raise TypeError("{} is not a relationship".format(fieldname))
        descriptor = getattr(self.model, fieldname)
        if fieldname in self.fk_fields:
            model = descriptor.field.rel.to
        else:
            model = descriptor.related.field.model
        return self.__class__(model)
