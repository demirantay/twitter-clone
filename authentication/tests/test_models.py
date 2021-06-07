from django.test import TestCase
from django.contrib.auth.models import User
from .models import BasicUserProfile, Follower


# Testing the basic user profile
class TestBasicUserProfile(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        BasicUserProfile.objects.create(user=user)

    def test_to_string(self):
        user_profile = BasicUserProfile.objects.get(id=1)
        expected_to_string = "User: test_user"
        self.assertEqual(expected_to_string, str(user_profile))


# Testing the follower
class TestFollower(TestCase):
    def setUp(self):
        user_1 = User.objects.create(username='user_1', password='123')
        user_2 = User.objects.create(username='user_2', password='123')
        Follower.objects.create(following=user_1, follower=user_2)

    def test_to_string(self):
        follower_obj = Follower.objects.get(id=1)
        expected_to_string = "Following: user_1 | Follower: user_2"
        self.assertEqual(expected_to_string, str(follower_obj))
