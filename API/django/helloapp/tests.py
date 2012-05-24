"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HelloWorldTest(TestCase):
    """
    HelloWorldTest
    Basic Test for Stack testing. Should return some data out of the postgresql db.
    Including a GEO Address (Something like 42.1123123, 24.12312312) and Hello World.
    """
    def testHelloWorld(self):
        return "Hello World"
