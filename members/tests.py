from members.models import UserProfile
from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserCreationTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_user_is_created(self):
        user_object_name = User.objects.get(username="john")
        user_profile_name = UserProfile.objects.get(user="1")
        self.assertEqual(str(user_object_name), "john")
        self.assertEqual(str(user_profile_name), "john")


class UserProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        test_user = UserProfile.objects.get(user="1")
        test_user.user_bio = "Hello, World!"
        test_user.save()

    def test_userbio_is_created(self):
        test_user = UserProfile.objects.get(user="1")
        user_bio = str(test_user.user_bio)
        self.assertEqual(user_bio, "Hello, World!")


class UserLoginTestCase(TestCase):

    # Account activation needs email verification.
    # Upon the test account creation, there is no
    # verification so the account is not active.
    # So we assert false.

    def setUp(self):
        self.client = Client(SERVER_NAME="localhost")
        self.credentials = {
            "username": "john",
            "password": "johnpassword",
        }
        user = User.objects.create_user(username="john")
        user.set_password("johnpassword")
        user.save()

    def test_user_login(self):
        login_response = self.client.post(
            "/members/login/", self.credentials, follow=True
        )
        self.assertFalse(login_response.context["user"].is_active)
