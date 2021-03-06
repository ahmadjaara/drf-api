from django.test import TestCase
from .models import Thing

# Testing the model
class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testthing = Thing.objects.create(name = "test_thing", description="Testing thing")
        testthing.save()


    def test_things_model(self):
        thing = Thing.objects.get(id=1)
        actual_title = thing.name
        self.assertEqual(actual_title, "test_thing")