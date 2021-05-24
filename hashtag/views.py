# Main Imports
import random

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile, Follower
from home.models import Tweet, TweetLike, TweetComment
from .models import Topic

from utils.session_utils import get_current_user, get_current_user_profile
from utils.base_utils import left_nav_tweet_form_processing
from utils.base_utils import mobile_tweet_form_processing
from utils.base_utils import get_who_to_follow
from utils.base_utils import get_topics_to_follow


def explore(request):
    """in this page the users can see the explore landing page"""

    # admin user session pop
    # admin user session pop
    # Deleting any sessions regarding top-tier type of users

    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # Topics to follow
    topics_to_follow = get_topics_to_follow(Topic, ObjectDoesNotExist, random)

    # Who to follow box cells
    who_to_follow = get_who_to_follow(
        BasicUserProfile, ObjectDoesNotExist, random
    )

    # Getting the last 10 tweets of each topic
    topics_tweets = {}

    for topic in topics_to_follow:
        topics_tweet_query = Tweet.objects.filter(
            topic=topic
        )[:10]
        topics_tweets[topic.id] = topics_tweet_query

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "topics_tweets": topics_tweets,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "hashtag/explore.html", data)


def topic_explore(request, topic):
    """aa"""

    data = {}

    return render(request, "hashtag/topic_explore.html", data)
