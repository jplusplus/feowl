from django.utils import unittest
from django.test.client import Client
from models import PowerReport, Area
from django.contrib.auth.models import User
from tastypie_test import ResourceTestCase
from django.db import models
from tastypie.models import create_api_key
from django.contrib.auth.models import Permission
import json

models.signals.post_save.connect(create_api_key, sender=User)


class PowerReportTest(unittest.TestCase):
    def test_basic(self):
        """
        Test basic creation of one object
        """

        #create dummy data
        PowerReport(
            location='POINT(151.207555, -33.88576)',
            duration=250,
        )

        self.assertEqual(1, 1)


class PowerReportResourceTest(ResourceTestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        super(PowerReportResourceTest, self).setUp()

        # Create a user.
        self.username = u'john'
        self.password = u'doe'
        self.user = User.objects.create_user(self.username, 'john@example.com', self.password)
        self.api_key = self.user.api_key.key
        self.c = Client()
        self.post_data = {
           "area": {"pk": 1},
           "happened_at": "2012-06-14T12:37:50+00:00",
           "has_experienced_outage": True,
           "duration": 60
        }

        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        self.power_report_1 = PowerReport.objects.get(duration=121)

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.detail_url = '/api/v1/reports/{0}/'.format(self.power_report_1.pk)

    def get_credentials(self):
        return {"username": self.username, "api_key": self.api_key}

    def test_get_list_unauthorzied(self):
        """Get reports from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get('/api/v1/reports/'))

    def test_get_list_json(self):
        """Get reports from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get('/api/v1/reports/', self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 5)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'area': u'/api/v1/areas/1/',
            'happened_at': u'2012-06-13T12:37:50+00:00',
            'has_experienced_outage': True,
            'location': None,
            'duration': 240,
            'quality': u'1.00',
            'resource_uri': u'/api/v1/reports/2/'
        })

    def test_get_detail_unauthenticated(self):
        """Try to Get a single report from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single report from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['area', 'happened_at', 'has_experienced_outage', 'location', 'duration', 'quality', 'resource_uri'])
        self.assertEqual(self.deserialize(resp)['duration'], 121)

    def test_post_list_unauthenticated(self):
        """Try to Post a single report to the API without authenticated"""
        self.assertHttpUnauthorized(self.c.post('/api/v1/reports/', data=self.post_data))

    def test_post_list_without_permissions(self):
        """Post a single report to the API with authenticated and without add permissions"""
        # Check how many are there first.
        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpUnauthorized(self.c.post('/api/v1/reports/?user_name=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))
        # Verify that nothing was added to the db
        self.assertEqual(PowerReport.objects.count(), 5)

    def test_post_list_with_permissions(self):
        """Post a single report to the API with authenticated and with add permissions"""
        add_powerreport = Permission.objects.get(codename="add_powerreport")
        self.user.user_permissions.add(add_powerreport)
        # Check how many are there first.
        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpCreated(self.c.post('/api/v1/reports/?user_name=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))
        # Verify a new one has been added.
        self.assertEqual(PowerReport.objects.count(), 6)

    def test_put_detail_unauthenticated(self):
        """Put a single report is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.put(self.detail_url))

    def test_put_detail(self):
        """Put a single report is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.put(self.detail_url, self.get_credentials()))

    def test_delete_detail_unauthenticated(self):
        """Delete a single report is not allowed from the API without authenticated"""
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url))

    def test_delete_detail(self):
        """Delete a single report is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url, self.get_credentials()))


class AreaResourceTest(ResourceTestCase):

    def setUp(self):
        super(AreaResourceTest, self).setUp()

        # Create a user.
        self.username = u'john'
        self.password = u'doe'
        self.user = User.objects.create_user(self.username, 'john@example.com', self.password)
        self.api_key = self.user.api_key.key
        self.c = Client()
        self.post_data = {
            'city': 'Douala',
            'country': 'Cameroon',
            'name': 'Douala VI',
            'pop_per_sq_km': '12323.00',
        }

        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        self.area_1 = Area.objects.get(name="Douala I")

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.detail_url = '/api/v1/areas/{0}/'.format(self.area_1.pk)

    def get_credentials(self):
        return {"user_name": self.username, "api_key": self.api_key}

    def test_get_list_unauthorzied(self):
        """Get areas from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get('/api/v1/areas/'))

    def test_get_list_json(self):
        """Get areas from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get('/api/v1/areas/', self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 5)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'city': 'Douala',
            'country': 'Cameroon',
            'name': 'Douala I',
            'pop_per_sq_km': '223214.00',
            'resource_uri': '/api/v1/areas/1/'
        })

    def test_get_detail_unauthenticated(self):
        """Try to Get a single area from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single area from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['city', 'country', 'name', 'pop_per_sq_km', 'resource_uri'])
        self.assertEqual(self.deserialize(resp)['name'], "Douala I")

    def test_post_list_unauthenticated(self):
        """Try to Post a single area to the API without authenticated"""
        self.assertHttpMethodNotAllowed(self.c.post('/api/v1/areas/', data=self.post_data))

    def test_post_list(self):
        """Try to Post a single area to the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.post('/api/v1/areas/?user_name=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))

    def test_put_detail_unauthenticated(self):
        """Try to Put a single area is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.put(self.detail_url))

    def test_put_detail(self):
        """Try to Put a single area is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.put(self.detail_url, self.get_credentials()))

    def test_delete_detail_unauthenticated(self):
        """Try to Delete a single area is not allowed from the API without authenticated"""
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url))

    def test_delete_detail(self):
        """Try to Delete a single area is not allowed from the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url, self.get_credentials()))
