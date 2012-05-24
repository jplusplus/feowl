from django.test import TestCase

class HelloFeowlTest(TestCase):
    def test_basic_stack(self):
        """
        Test that we get some data, so we are testing the api and database stack
        """
        
        #create dummy data
        HelloWorld(text_1 = 'Hello', text_2 = 'World', int_1 = 1,
            geographic_point_1 = Point(151.207555, -33.88576), date_1 = timezone.now()
        )

        #use api method to get data again