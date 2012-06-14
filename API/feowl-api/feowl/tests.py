from django.utils import unittest
from django.test.client import Client
from models import PowerReport
import datetime
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

        add_powerreport = Permission.objects.get(codename="add_powerreport")
        self.user.user_permissions.add(add_powerreport)

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
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/reports/', format='json'))

    def test_get_list_json(self):
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
        self.assertHttpUnauthorized(self.api_client.get(self.detail_url, format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

    #     # # We use ``assertKeys`` here to just verify the keys, not all the data.
    #     # self.assertKeys(self.deserialize(resp), ['created', 'slug', 'title', 'user'])
    #     # self.assertEqual(self.deserialize(resp)['name'], 'First post')

    def test_post_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/reports/', format='json', data=self.post_data))

    def test_post_list(self):
        # Check how many are there first.
        self.assertEqual(PowerReport.objects.count(), 5)
        data = self.post_data
        self.assertHttpCreated(self.c.post('/api/v1/reports/?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(data), content_type="application/json"))
        # Verify a new one has been added.
        self.assertEqual(PowerReport.objects.count(), 6)

    def test_put_detail_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.put(self.detail_url, format='json', data={}))

    def test_put_detail(self):
        # Grab the current data & modify it slightly.
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
        new_data = original_data.copy()
        new_data['title'] = 'Updated: First Post'
        new_data['created'] = '2012-05-01T20:06:12'

        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
        # Make sure the count hasn't changed & we did an update.
        self.assertEqual(PowerReport.objects.count(), 5)
        # Check for updated data.
        self.assertEqual(PowerReport.objects.get(pk=25).title, 'Updated: First Post')
        self.assertEqual(PowerReport.objects.get(pk=25).slug, 'first-post')
        self.assertEqual(PowerReport.objects.get(pk=25).created, datetime.datetime(2012, 3, 1, 13, 6, 12))

    def test_delete_detail_unauthenticated(self):
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url))

    def test_delete_detail(self):
        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpMethodNotAllowed(self.c.delete(self.detail_url, self.get_credentials()))
