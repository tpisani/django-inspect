from django.test import TestCase

from django_inspect import Inspect
from django_inspect.tests.models import NotADjangoModel, InspectModel


class InspectTests(TestCase):

    def setUp(self):
        self.inspect = Inspect(InspectModel)

    def test_should_raise_typeerror_when_given_a_non_django_model(self):
        self.assertRaises(TypeError, Inspect, NotADjangoModel)

    def test_fields(self):
        self.assertEqual(self.inspect.fields, ["id",
                                               "int",
                                               "char",
                                               "text",
                                               "direct_fk"])

    def test_fk_fields(self):
        self.assertEqual(self.inspect.fk_fields, ["anotherfk_set",
                                                  "direct_fk",
                                                  "fk_set"])

    def test_m2m_fields(self):
        self.assertEqual(self.inspect.m2m_fields, ["manytomany_set"])
