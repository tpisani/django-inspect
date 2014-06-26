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
                                               "text"])

    def test_local_fields(self):
        self.assertEqual(self.inspect.local_fields, ["id",
                                                     "int",
                                                     "char",
                                                     "text",
                                                     "direct_fk",
                                                     "many_to_many"])

    def test_fk_fields(self):
        self.assertEqual(self.inspect.fk_fields, ["direct_fk"])

    def test_backwards_fk_fields(self):
        self.assertEqual(self.inspect.backwards_fk_fields, ["fk_set",
                                                            "anotherfk_set"])

    def test_all_fk_fields(self):
        self.assertEqual(self.inspect.all_fk_fields, ["direct_fk",
                                                      "fk_set",
                                                      "anotherfk_set"])

    def test_m2m_fields(self):
        self.assertEqual(self.inspect.m2m_fields, ["many_to_many"])

    def test_backwards_m2m_fields(self):
        self.assertEqual(self.inspect.backwards_m2m_fields, ["manytomany_set"])

    def test_all_m2m_fields(self):
        self.assertEqual(self.inspect.all_m2m_fields, ["many_to_many",
                                                       "manytomany_set"])
