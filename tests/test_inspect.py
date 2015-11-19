from django.test import TestCase

from django_inspect import Inspect

from tests.test_app.models import NotADjangoModel, InspectModel


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
                                               "direct_fk",
                                               "many_to_many"])

    def test_non_rel_fields(self):
        self.assertEqual(self.inspect.non_rel_fields, ["id",
                                                       "int",
                                                       "char",
                                                       "text"])

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

    def test_all_fields(self):
        self.assertEqual(self.inspect.all_fields, ["id",
                                                   "int",
                                                   "char",
                                                   "text",
                                                   "direct_fk",
                                                   "many_to_many",
                                                   "fk_set",
                                                   "anotherfk_set",
                                                   "manytomany_set"])

    def test_sub_inspect_should_raise_typeerror_when_given_a_non_rel_field(self):
        self.assertRaises(TypeError, self.inspect.sub_inspect, "char")

    def test_sub_inspect(self):
        direct_fk_inspect = self.inspect.sub_inspect("direct_fk")
        self.assertEqual(direct_fk_inspect.all_fields, ["id",
                                                        "bigint",
                                                        "boolean",
                                                        "inspectmodel_set"])

    def test_sub_inspect_backwards_field(self):
        manytomany_set_inspect = self.inspect.sub_inspect("manytomany_set")
        self.assertEqual(manytomany_set_inspect.all_fields, ["id",
                                                             "inspect_model"])

    def test_sub_inspect_by_path(self):
        path_inspect = self.inspect.sub_inspect("many_to_many.some_item")
        self.assertEqual(path_inspect.all_fields, ["id",
                                                   "date",
                                                   "decimal",
                                                   "anothermanytomany_set"])
