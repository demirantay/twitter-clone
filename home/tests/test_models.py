from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tweet, TweetComment, TweetLike, TweetCommentLike


# Test tweet model
class TestTweet(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        Tweet.objects.create(user=user, content="foo")

    def test_to_string(self):
        tweet = Tweet.objects.get(id=1)
        expected_to_string = "Tweet id: 1"
        self.assertEqual(expected_to_string, str(tweet))


# Test tweetcomment model
class TestTweetComment(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        tweet = Tweet.objects.create(user=user, content="foo")
        TweetComment.objects.create(tweet=tweet, content="foo", commentor=user)

    def test_to_string(self):
        comment = TweetComment.objects.get(id=1)
        expected_to_string = "Comment id: 1"
        self.assertEqual(expected_to_string, str(comment))
