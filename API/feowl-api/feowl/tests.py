from django.test.client import Client
from models import PowerReport, Area, Contributor, Device
from django.contrib.auth.models import User, Permission
from tastypie_test import ResourceTestCase
from django.db import models
from tastypie.models import create_api_key
import json
from django.conf import settings

models.signals.post_save.connect(create_api_key, sender=User)


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
           "area": "/api/v1/areas/1/",
           "happened_at": "2012-06-14 12:37:50",
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

    def test_get_list_unauthorizied(self):
        """Get reports from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get('/api/v1/reports/'))

    def test_get_list_json(self):
        """Get reports from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get('/api/v1/reports/', self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 5)
        # Here we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'area': '/api/v1/areas/1/',
            'happened_at': '2012-06-13T12:37:50+00:00',
            'has_experienced_outage': True,
            'location': None,
            'duration': 240,
            'quality': '1.00',
            'resource_uri': '/api/v1/reports/2/',
            'contributor': None,
            'device': None
        })

    def test_header_auth(self):
        resp = self.c.get(self.detail_url, **{'HTTP_AUTHORIZATION': 'ApiKey ' + self.username + ':' + self.api_key})
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['area', 'happened_at', 'has_experienced_outage', 'contributor', 'device', 'location', 'duration', 'quality', 'resource_uri'])
        self.assertEqual(self.deserialize(resp)['duration'], 121)

    def test_get_detail_unauthenticated(self):
        """Try to Get a single report from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single report from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['area', 'happened_at', 'has_experienced_outage', 'contributor', 'device', 'location', 'duration', 'quality', 'resource_uri'])
        self.assertEqual(self.deserialize(resp)['duration'], 121)

    def test_get_detail_csv(self):
        """Get a single report from the API with authenticated. With checks if all keys are available"""
        content = 'area,contributor,device,happened_at,has_experienced_outage,location,duration,quality,resource_uri\r\n/api/v1/areas/1/,None,None,2012-06-13T09:56:25+00:00,True,POINT (10.0195312486050003 3.6011423196581309),121,1.00,/api/v1/reports/1/\r\n'
        resp = self.c.get('/api/v1/reports/1/?username=' + self.username + '&api_key=' + self.api_key + '&format=csv')
        self.assertEquals(resp.content, content)

    def test_get_list_csv(self):
        """Get a single report from the API with authenticated. With checks if all keys are available"""
        content = 'area,contributor,device,happened_at,has_experienced_outage,location,duration,quality,resource_uri\r\n/api/v1/areas/1/,None,None,2012-06-13T12:37:50+00:00,True,None,240,1.00,/api/v1/reports/2/\r\n/api/v1/areas/5/,None,None,2012-06-13T12:38:06+00:00,True,None,32,1.00,/api/v1/reports/3/\r\n/api/v1/areas/2/,None,None,2012-06-13T12:38:18+00:00,True,None,1231,1.00,/api/v1/reports/4/\r\n/api/v1/areas/2/,None,None,2012-06-13T12:38:27+00:00,True,None,564,1.00,/api/v1/reports/5/\r\n/api/v1/areas/1/,None,None,2012-06-13T09:56:25+00:00,True,POINT (10.0195312486050003 3.6011423196581309),121,1.00,/api/v1/reports/1/\r\n'
        resp = self.c.get('/api/v1/reports/?username=' + self.username + '&api_key=' + self.api_key + '&format=csv')
        self.assertEquals(resp.content, content)

    def test_post_list_unauthenticated(self):
        """Try to Post a single report to the API without authenticated"""
        self.assertHttpUnauthorized(self.c.post('/api/v1/reports/', data=self.post_data))

    def test_post_list_without_permissions(self):
        """Post a single report to the API with authenticated and without add permissions"""
        add_powerreport = Permission.objects.get(codename="add_powerreport")
        self.user.user_permissions.remove(add_powerreport)
        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpUnauthorized(self.c.post('/api/v1/reports/?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))
        # Verify that nothing was added to the db
        self.assertEqual(PowerReport.objects.count(), 5)

    def test_post_list_with_permissions(self):
        """Post a single report to the API with authenticated and with add permissions"""
        add_powerreport = Permission.objects.get(codename="add_powerreport")
        self.user.user_permissions.add(add_powerreport)
        # Check how many there are first.
        self.assertEqual(PowerReport.objects.count(), 5)
        self.assertHttpCreated(self.c.post('/api/v1/reports/?username=%s&api_key=%s' % (self.username, self.api_key), data=json.dumps(self.post_data), content_type="application/json"))
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
            'overall_population': 200000
        }

        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        self.area_1 = Area.objects.get(name="Douala I")

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.detail_url = '/api/v1/areas/{0}/'.format(self.area_1.pk)

    def get_credentials(self):
        return {"username": self.username, "api_key": self.api_key}

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
            'pop_per_sq_km': '0.00',
            'overall_population': 223214,
            'resource_uri': '/api/v1/areas/1/',
            'id': '1'
        })

    def test_get_detail_unauthenticated(self):
        """Try to Get a single area from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single area from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['id', 'city', 'country', 'name', 'pop_per_sq_km', 'overall_population', 'resource_uri'])
        self.assertEqual(self.deserialize(resp)['name'], "Douala I")

    def test_post_list_unauthenticated(self):
        """Try to Post a single area to the API without authenticated"""
        self.assertHttpMethodNotAllowed(self.c.post('/api/v1/areas/', data=self.post_data))

    def test_post_list(self):
        """Try to Post a single area to the API with authenticated"""
        self.assertHttpMethodNotAllowed(self.c.post('/api/v1/areas/?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))

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


class ContributorResourceTest(ResourceTestCase):

    def setUp(self):
        super(ContributorResourceTest, self).setUp()

        # Create a user.
        self.username = u'john'
        self.password = u'doe'
        self.email = u'john@example.com'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.api_key = self.user.api_key.key
        self.c = Client()
        self.post_data = {
            'name': 'james',
            'email': 'james@example.com',
            'password': self.user.__dict__["password"],
            'language': 'DE'
        }
        self.put_data = {
            'email': 'jonny@example.com',
            'language': 'DE'
        }

        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        Contributor(name="Tobias", email="tobias@test.de").save()
        self.contributor_1 = Contributor.objects.get(pk=1)

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.list_url = '/api/v1/contributors/'
        self.detail_url = '{0}{1}/'.format(self.list_url, self.contributor_1.pk)

    def get_credentials(self):
        return {"username": self.username, "api_key": self.api_key}

    def test_get_list_unauthorzied(self):
        """Get areas from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.list_url))

    def test_get_list_json(self):
        """Get users from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.list_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'id': '1',
            'name': 'Tobias',
            'email': 'tobias@test.de',
            'password': settings.DUMMY_PASSWORD,
            'resource_uri': self.detail_url,
            'language': 'EN'  # EN is the default value
        })

    def test_get_detail_unauthenticated(self):
        """Try to Get a single user from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single user from the API with authenticated. With checks if all keys are available"""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['id', 'name', 'email', 'password', 'resource_uri', 'language'])
        self.assertEqual(self.deserialize(resp)['name'], "Tobias")

    def test_post_list_unauthenticated(self):
        """Try to Post a single user to the API without authenticated"""
        self.assertHttpUnauthorized(self.c.post(self.list_url, data=self.post_data))

    def test_post_list_without_permissions(self):
        """Try to Post a single user to the API with authenticated and without permission"""
        self.assertHttpUnauthorized(self.c.post(self.list_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))

    def test_post_list_with_permissions(self):
        """Try to Post a single user to the API with authenticated and permission"""
        add_contributor = Permission.objects.get(codename="add_contributor")
        self.user.user_permissions.add(add_contributor)
        self.assertEqual(Contributor.objects.count(), 1)
        self.assertHttpCreated(self.c.post(self.list_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))
        self.assertEqual(Contributor.objects.count(), 2)

    def test_put_detail_unauthenticated(self):
        """Try to Put a single user is not allowed from the API with authenticated"""
        self.assertHttpUnauthorized(self.c.put(self.detail_url))

    def test_put_detail_without_permission(self):
        """Try to Put a single user is not allowed from the API with authenticated and without permission"""
        self.assertHttpUnauthorized(self.c.put(self.detail_url, self.get_credentials()))

    def test_put_detail_with_permission(self):
        """Try to Put a single user is not allowed from the API with authenticated abd permission"""
        change_contributor = Permission.objects.get(codename="change_contributor")
        self.user.user_permissions.add(change_contributor)
        self.assertEqual(Contributor.objects.count(), 1)
        self.assertHttpAccepted(self.c.put(self.detail_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.put_data), content_type="application/json"))
        self.assertEqual(Contributor.objects.count(), 1)
        self.assertEqual(Contributor.objects.get(pk=self.contributor_1.pk).email, self.put_data.get("email"))

    def test_delete_detail_unauthenticated(self):
        """Delete a single user is not allowed from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.delete(self.detail_url))

    def test_delete_detail_without_permission(self):
        """Delete a single user is allowed from the API with authenticated"""
        self.assertEqual(Contributor.objects.count(), 1)
        self.assertHttpUnauthorized(self.c.delete(self.detail_url, self.get_credentials()))
        self.assertEqual(Contributor.objects.count(), 1)

    def test_delete_detail_with_permision(self):
        """Delete a single user is allowed from the API with authenticated"""
        delete_contributor = Permission.objects.get(codename="delete_contributor")
        self.user.user_permissions.add(delete_contributor)
        self.assertEqual(Contributor.objects.count(), 1)
        self.assertHttpAccepted(self.c.delete(self.detail_url, self.get_credentials()))
        self.assertEqual(Contributor.objects.count(), 0)


class DeviceResourceTest(ResourceTestCase):

    def setUp(self):
        super(DeviceResourceTest, self).setUp()

        # Create a user.
        self.username = u'john'
        self.password = u'doe'
        self.email = u'john@example.com'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.api_key = self.user.api_key.key
        self.c = Client()
        self.post_data = {
            'category': 'SubDevice',
            'phone_number': '12381294323',
        }
        self.put_data = {
            'phone_number': "4267486238"
        }

        Contributor(name="Tobias", email="tobias@test.de").save()
        self.contributor = Contributor.objects.get(pk=1)

        Device(phone_number="01234567890", category="MainDevice", contributor=self.contributor).save()
        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        self.device_1 = Device.objects.get(pk=1)

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.list_url = u'/api/v1/devices/'
        self.detail_url = u'{0}{1}/'.format(self.list_url, self.device_1.pk)
        self.user_url = u'/api/v1/contributors/{0}/'.format(self.contributor.id)

    def get_credentials(self):
        return {"username": self.username, "api_key": self.api_key}

    def test_get_list_unauthorzied(self):
        """Get devices from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.get(self.list_url))

    def test_get_list_json(self):
        """Get devices from the API with authenticated. With checks if all keys are available."""
        resp = self.c.get(self.list_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            u"category": u"MainDevice",
            u"phone_number": u"01234567890",
            u"resource_uri": self.detail_url,
            u"contributor": self.user_url
        })

    def test_get_detail_unauthenticated(self):
        """Try to Get a single device from the API without authentication"""
        self.assertHttpUnauthorized(self.c.get(self.detail_url))

    def test_get_detail_json(self):
        """Get a single device from the API with authentication. Also checks if all keys are available."""
        resp = self.c.get(self.detail_url, self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['category', 'phone_number', 'resource_uri', 'contributor'])
        self.assertEqual(self.deserialize(resp)['category'], "MainDevice")

    def test_post_list_unauthenticated(self):
        """Try to Post a single device to the API without authenticated"""
        self.assertHttpUnauthorized(self.c.post(self.list_url, data=self.post_data))

    def test_post_list_without_permissions(self):
        """Try to Post a single device to the API with authenticated and without permission"""
        self.assertHttpUnauthorized(self.c.post(self.list_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))

    def test_post_list_with_permissions(self):
        """Post a single device to the API with authenticated and permission"""
        add_device = Permission.objects.get(codename="add_device")
        self.user.user_permissions.add(add_device)
        self.assertEqual(Device.objects.count(), 1)
        self.assertHttpCreated(self.c.post(self.list_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.post_data), content_type="application/json"))
        self.assertEqual(Device.objects.count(), 2)

    def test_put_detail_unauthenticated(self):
        """Try to Put a single device is not allowed from the API with authenticated"""
        self.assertHttpUnauthorized(self.c.put(self.detail_url))

    def test_put_detail_without_permission(self):
        """Try to Put a single device is not allowed from the API with authenticated and without permission"""
        self.assertHttpUnauthorized(self.c.put(self.detail_url, self.get_credentials()))

    def test_put_detail_with_permission(self):
        """Put a single device is not allowed from the API with authenticated abd permission"""
        change_device = Permission.objects.get(codename="change_device")
        self.user.user_permissions.add(change_device)
        self.assertEqual(Device.objects.count(), 1)
        self.assertHttpAccepted(self.c.put(self.detail_url + '?username=' + self.username + '&api_key=' + self.api_key, data=json.dumps(self.put_data), content_type="application/json"))
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.get(pk=self.device_1.pk).phone_number, self.put_data.get("phone_number"))

    def test_delete_detail_unauthenticated(self):
        """Delete a single device is not allowed from the API without authenticated"""
        self.assertHttpUnauthorized(self.c.delete(self.detail_url))

    def test_delete_detail_without_permission(self):
        """Delete a single device is not allowed from the API with authenticated and without permission"""
        self.assertHttpUnauthorized(self.c.delete(self.detail_url, self.get_credentials()))

    def test_delete_detail_with_permission(self):
        """Delete a single device is not allowed from the API with authenticated and permission"""
        delete_device = Permission.objects.get(codename="delete_device")
        self.user.user_permissions.add(delete_device)
        self.assertEqual(Device.objects.count(), 1)
        self.assertHttpAccepted(self.c.delete(self.detail_url, self.get_credentials()))
        self.assertEqual(Device.objects.count(), 0)
