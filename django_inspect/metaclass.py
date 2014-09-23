from django.db.models.base import ModelBase

from django_inspect import Inspect


class InspectMetaclass(ModelBase):
    """
    Simple metaclass for easily attaching Inspect instances to models.
    """

    @staticmethod
    def contribute_to_class(cls, name):
        cls.inspect = Inspect(cls)
