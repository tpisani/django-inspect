from django.test import TestCase

from django_inspect import Inspect

from tests.test_app.models import InspectableModel


class InspectMetaclassTests(TestCase):

    def setUp(self):
        self.inspectable = InspectableModel()

    def test_model_should_have_inspect_instance_attached(self):
        self.assertIsInstance(self.inspectable.inspect, Inspect)

    def test_inspect_instance_should_have_been_created_with_that_model(self):
        self.assertEqual(self.inspectable.inspect.model, InspectableModel)
