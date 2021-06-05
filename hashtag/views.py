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
from notification.models import NotificationLike

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


def topic_explore(request, topic, page):
    """in this page the users can see a topics tweet feed"""
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

    # Get the current topic
    try:
        current_topic = Topic.objects.get(name=topic)
    except ObjectDoesNotExist:
        current_topic = None

    # Get the topics tweets and add the pagination cutoff points for the
    # current page tweets
    current_page = page
    previous_page = page-1
    next_page = page+1

    post_records_starting_point = current_page * 46
    post_records_ending_point = post_records_starting_point + 46

    try:
        tweet_feed = Tweet.objects.filter(
            topic=current_topic
        ).order_by("-id")
    except ObjectDoesNotExist:
        tweet_feed = None

    tweet_feed = tweet_feed[post_records_starting_point:post_records_ending_point]

    # comment form processing
    if request.POST.get("single_topic_explore_tweet_cell_comment_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        return HttpResponseRedirect("/tweet/" + str(current_tweet_id) + "/")

    # tweet like form processing
    if request.POST.get("single_topic_explore_tweet_cell_like_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        current_tweet = Tweet.objects.get(id=current_tweet_id)
        new_like = TweetLike(
            tweet=current_tweet,
            liker=current_basic_user_profile
        )
        new_like.save()
        current_tweet.tweet_like_amount += 1
        current_tweet.save()
        new_notification = NotificationLike(
            notified=current_tweet.user,
            notifier=current_basic_user_profile,
            tweet=current_tweet,
        )
        new_notification.save()
        return HttpResponseRedirect("/tweet/" + str(current_tweet.id) + "/")

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "current_topic": current_topic,
        "current_page": page,
        "previous_page": previous_page,
        "next_page": next_page,
        "tweet_feed": tweet_feed,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "hashtag/topic_explore.html", data)
