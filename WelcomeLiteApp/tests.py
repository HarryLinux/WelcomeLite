from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class JobOfferIndexViewTests(TestCase):
    def test_no_job_offers(self):
        """
        If no job offers exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('welcome:index'))
        self.assertContains(response, "No job offers available")
