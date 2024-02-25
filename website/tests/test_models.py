
from django.conf import settings
from django.test import TestCase

from website.models import Venue, Author


class ModelsTests(TestCase):
    def test_venue_string_representation(self):
        venue = Venue(city="London", country="United Kingdom")
        self.assertEqual(str(venue), "London, United Kingdom")

