from django.db import models


class NotADjangoModel(object):
    pass


class InspectModel(models.Model):
    int = models.IntegerField()
    char = models.CharField()
    text = models.TextField()
    direct_fk = models.ForeignKey("DirectFK")
    many_to_many = models.ManyToManyField("AnotherManyToMany")


class FK(models.Model):
    inspect_model = models.ForeignKey(InspectModel)


class AnotherFK(models.Model):
    inspect_model = models.ForeignKey(InspectModel)


class DirectFK(models.Model):
    pass


class ManyToMany(models.Model):
    inspect_model = models.ManyToManyField(InspectModel)


class AnotherManyToMany(models.Model):
    pass
