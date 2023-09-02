from django.test import TestCase
from django.contrib.auth import get_user_model
from moneyed import Money
from .models import Donation
from django.test import Client

# Create your tests here.

class DonationsTests(TestCase):

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        username = "testuser_1001"
        password = "s897yuP&&+?12"
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )
        self.client.force_login(self.user)

    """Test for creating a donation"""
    def test_create_donation(self):
        amount = Money(1000, 'USD')
        frequency = 'One-time'

        # create donation object 1
        donation1 = Donation.objects.create(amount=amount, frequency=frequency, user=self.user)

        self.assertEqual(donation1.name, 'Volunteer App Donation')
        self.assertEqual(str(donation1.get_currency()), 'USD')
        self.assertEqual(donation1.get_amount(), 1000)
        self.assertEqual(donation1.frequency, 'One-time')

        amount2 = Money(200, 'GBP')
        frequency2 = 'Monthly'
        name = 'Monthly donation'

        # create donation object 2
        donation2 = Donation.objects.create(name=name, amount=amount2, frequency=frequency2, user=self.user)

        self.assertEqual(donation2.name, name)
        self.assertEqual(str(donation2.get_currency()), 'GBP')
        self.assertEqual(donation2.get_amount(), 200)
        self.assertEqual(donation2.frequency, 'Monthly')

        # make sure Donations are ordered by creation date
        self.assertEqual(Donation.objects.all()[0], donation2)
