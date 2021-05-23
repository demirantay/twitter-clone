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
from utils.base_utils import left_nav_tweet_form_processing
from utils.base_utils import mobile_tweet_form_processing
from utils.base_utils import get_who_to_follow
from utils.base_utils import get_topics_to_follow


def home(request, page):
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
    left_nav_tweet_form_processing(request, Tweet, current_basic_user_profile)

    # Mobile Tweet Form processing
    mobile_tweet_form_processing(request, Tweet, current_basic_user_profile)

    # Topics to follow
    topics_to_follow = get_topics_to_follow(Topic, ObjectDoesNotExist, random)

    # Search form processing
    if request.POST.get("right_nav_search_submit_btn"):
        search_input = request.POST.get("search_input")
        return HttpResponseRedirect("/search/" + str(search_input) + "/")

    # Who to follow box cells
    who_to_follow = get_who_to_follow(
        BasicUserProfile, ObjectDoesNotExist, random
    )

    if request.POST.get("base_who_to_follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        followed_user = BasicUserProfile.objects.get(id=hidden_user_id)

        # check if the followed user is in followings of current user
        all_followings = Follower.objects.filter(
            follower=current_basic_user_profile
        )

        for following in all_followings:
            if following.following == followed_user:
                pass
            else:
                new_follow = Follower(
                    following=followed_user, follower=current_basic_user_profile,
                )
                new_follow.save()

        return HttpResponseRedirect(
            "/profile/" + followed_user.user.username + "/"
        )

    # ----- base values ending point  ---------

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
    # At every page there will be 45 entries so always multiply it by that and
    # then reduce your objects
    current_page = page
    previous_page = page-1
    next_page = page+1

    post_records_starting_point = current_page * 46
    post_records_ending_point = post_records_starting_point + 46

    tweet_feed = []

    try:
        all_tweets = Tweet.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None

    for tweet in all_tweets:
        for following in all_followings:
            if tweet.user == following.following:
                tweet_feed.append(tweet)

    tweet_feed = tweet_feed[post_records_starting_point:post_records_ending_point]


    # Getting the comment amount for each tweet
    tweet_comment_amounts = {}
    for tweet in tweet_feed:
        tweet_comments = TweetComment.objects.filter(tweet=tweet)
        amount = len(tweet_comments)
        tweet_comment_amounts[tweet.id] = amount

    # Getting the likes for each tweet
    tweet_like_amounts = {}
    for tweet in tweet_feed:
        tweet_likes = TweetLike.objects.filter(tweet=tweet)
        amount = len(tweet_likes)
        tweet_like_amounts[tweet.id] = amount

    # Comment Form Processing
    if request.POST.get("tweet_cell_comment_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        current_tweet = Tweet.objects.get(id=current_tweet_id)
        return HttpResponseRedirect("/tweet/" + str(current_tweet.id) + "/")

    # Like Form Processing
    if request.POST.get("tweet_cell_like_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        current_tweet = Tweet.objects.get(id=current_tweet_id)
        new_like = TweetLike(
            tweet=current_tweet,
            liker=current_basic_user_profile
        )
        new_like.save()
        return HttpResponseRedirect("/tweet/" + str(current_tweet.id) + "/")

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "tweet_feed": tweet_feed,
        "tweet_comment_amounts": tweet_comment_amounts,
        "tweet_like_amounts": tweet_like_amounts,
        "current_page": page,
        "previous_page": previous_page,
        "next_page": next_page,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "home/home.html", data)


def tweet_single(request, tweet_id):
    """.."""

    data = {}

    return render(request, "home/single_tweet.html", data)
