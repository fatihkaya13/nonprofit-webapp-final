from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
from django.test import Client

# Create your tests here.

class ProfileTests(TestCase):

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

    """Test Profile model and User"""
    def test_create_user(self):
        """Test creating a user with password is successful"""
        username = "testuser_1002"
        password = "s897yuP&&+?13"
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_profile(self):
        """Test created user has a profile"""
        profile = Profile.objects.get(user=self.user)

        self.assertEqual(self.user.username, str(profile))

    def test_create_user_without_username_raises_error(self):
        """Test creating a user with missing username parameter raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "strongPassword+?12")

    def test_update_profile(self):
        """Test user can update profile"""
        profile = Profile.objects.get(user=self.user)
        profile.first_name = "Test User FirstName"
        profile.last_name = "Test User LastName"
        profile.biography = "I live for only test purposes in this life"
        profile.save()
        self.assertEqual(profile.first_name, "Test User FirstName")
        self.assertEqual(profile.last_name, "Test User LastName")
        self.assertEqual(profile.biography, "I live for only test purposes in this life")
