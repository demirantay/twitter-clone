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
from .models import Tweet, TweetLike, TweetComment
from hashtag.models import Topic

from utils.session_utils import get_current_user, get_current_user_profile


def home(request):
    """this is the homepage of the site and is an proxy redirector"""

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

    # Tweet form processing
    if request.POST.get("hidden_panel_tweet_submit_btn"):
        tweet_content = request.POST.get("tweet_content")
        tweet_image = request.FILES.get("tweet_image")

        new_tweet = Tweet(
            user=current_basic_user_profile, content=tweet_content,
            image=tweet_image
        )
        new_tweet.save()

    # Mobile Tweet Form processing
    if request.POST.get("mobile_hidden_tweet_submit_btn"):
        tweet_content = request.POST.get("tweet_content")
        tweet_image = request.FILES.get("tweet_image")

        new_tweet = Tweet(
            user=current_basic_user_profile, content=tweet_content,
            image=tweet_image
        )
        new_tweet.save()

    # Search form processing
    if request.POST.get("right_nav_search_submit_btn"):
        search_input = request.POST.get("search_input")
        return HttpResponseRedirect("/search/" + str(search_input) + "/")

    # Who to follow box cells
    try:
        latest_user = BasicUserProfile.objects.last()
    except ObjectDoesNotExist:
        latest_user = None

    number_1 = random.randint(1, latest_user.id)
    number_2 = random.randint(1, latest_user.id)
    number_3 = random.randint(1, latest_user.id)

    who_to_follow = []

    who_to_follow.append(BasicUserProfile.objects.get(id=number_1))
    who_to_follow.append(BasicUserProfile.objects.get(id=number_2))
    who_to_follow.append(BasicUserProfile.objects.get(id=number_3))

    if request.POST.get("base_who_to_follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        followed_user = BasicUserProfile.objects.get(id=hidden_user_id)

        new_follow = Follower(
            following=followed_user, follower=current_basic_user_profile,
        )
        new_follow.save()
        return HttpResponseRedirect(
            "/profile/" + followed_user.user.username + "/"
        )

    # Topics to follow
    try:
        all_topics = Topic.objects.all()
        latest_topic = Topic.objects.last()
    except ObjectDoesNotExist:
        all_topics = None
        latest_topic = None

    topics_to_follow = []

    for i in range(5):
        random_topic = all_topics[random.randint(1, latest_topic.id-1)]
        topics_to_follow.append(random_topic)

    # Home Page Tweet Form Processing
    if request.POST.get("home_page_tweet_form_submit_btn"):
        tweet_content = request.POST.get("tweet_content")
        tweet_image = request.FILES.get("tweet_image")

        new_tweet = Tweet(
            user=current_basic_user_profile, content=tweet_content,
            image=tweet_image
        )
        new_tweet.save()

        return HttpResponseRedirect("/")

    # Getting all Followings
    try:
        all_followings = Follower.objects.filter(
            follower=current_basic_user_profile
        )
    except ObjectDoesNotExist:
        all_followings = None

    # Get all the tweets of followings
    tweet_feed = []

    try:
        all_tweets = Tweet.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None

    for tweet in all_tweets:
        for following in all_followings:
            if tweet.user == following.following:
                tweet_feed.append(tweet)

    # Getting the comment amount for each tweet
    tweet_comment_amounts = {}
    for tweet in tweet_feed:
        tweet_comments = TweetComment.objects.filter(tweet=tweet)
        amount = len(tweet_comments)
        tweet_comment_amounts[tweet.id] = amount

    # Getting the likes for each tweet



    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "tweet_feed": tweet_feed,
        "tweet_comment_amounts": tweet_comment_amounts,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "home/home.html", data)
