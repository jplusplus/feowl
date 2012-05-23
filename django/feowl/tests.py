"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


# Need for later:
#  = HelloWorld(text_1 = 'Hello', text_2 = 'World', int_1 = 1, geographic_point_1 = Point(151.207555, -33.88576), date_1 = timezone.now())

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
