from django.test import TestCase
from models import Report
from datetime import datetime

class ReportsTest(TestCase):
    def test_basic_stack(self):
        """
        Test that we get some data, so we are testing the api and database stack
        """
        
        #create dummy data
        Report(
            createdAt = datetime.now(),
            modifiedAt = datetime.now(),
            reportType = 'power',
            location = 'Point(151.207555, -33.88576)'
        )

        #use api method to get data again
        #...