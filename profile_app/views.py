# Main Imports
import random

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile
from authentication.models import BasicUserProfile, Follower
from home.models import Tweet, TweetLike, TweetComment
from hashtag.models import Topic
from notification.models import NotificationLike

from utils.session_utils import get_current_user, get_current_user_profile
from utils.base_utils import left_nav_tweet_form_processing
from utils.base_utils import mobile_tweet_form_processing
from utils.base_utils import get_who_to_follow
from utils.base_utils import get_topics_to_follow


def profile(request):
    """in this view the users can see their own profile"""

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

    # Get the current user tweets
    try:
        all_tweets = Tweet.objects.filter(
            user=current_basic_user_profile
        ).order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None

    # Get the current_user followings and followers
    try:
        all_followers = Follower.objects.filter(
            following=current_basic_user_profile,
        )
    except ObjectDoesNotExist:
        all_followers = None

    try:
        all_followings = Follower.objects.filter(
            follower=current_basic_user_profile,
        )
    except ObjectDoesNotExist:
        all_followings = None

    # Tweet comment form processing
    if request.POST.get("profile_tweet_comment_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        return HttpResponseRedirect("/tweet/" + str(current_tweet_id) + "/")

    # Tweet like form processing
    if request.POST.get("profile_tweet_like_submit_btn"):
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
        "all_tweets": all_tweets,
        "tweet_amount": len(all_tweets),
        "follower_amount": len(all_followers),
        "following_amount": len(all_followings)
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "profile/profile.html", data)


def other_user_profile(request, other_user_username):
    """users can view other profles from here"""

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

    # Get other user
    try:
        other_user = User.objects.get(username=other_user_username)
    except ObjectDoesNotExist:
        other_user = None

    try:
        other_user_profile = BasicUserProfile.objects.get(user=other_user)
    except ObjectDoesNotExist:
        other_user_profile = None

    # if the user is none return to home
    if other_user == None:
        return HttpResponseRedirect("/")

    # Other user tweets
    try:
        all_tweets = Tweet.objects.filter(
            user=other_user_profile
        ).order_by("-id")
    except ObjectDoesNotExist:
        all_tweets = None

    # Get the other user followings and followers
    try:
        all_followers = Follower.objects.filter(
            following=other_user_profile,
        )
    except ObjectDoesNotExist:
        all_followers = None

    try:
        all_followings = Follower.objects.filter(
            follower=other_user_profile,
        )
    except ObjectDoesNotExist:
        all_followings = None

    # Profile follow form processing
    already_follower = False

    if request.POST.get("other_user_profile_follow_submit_btn"):
        is_follower = Follower.objects.filter(
            following=other_user_profile,
            follower=current_basic_user_profile,
        )
        if is_follower == None or is_follower == [] or bool(is_follower) == False:
            new_follower = Follower(
                following=other_user_profile,
                follower=current_basic_user_profile,
            )
            new_follower.save()
            return HttpResponseRedirect("/profile/"+other_user.username+"/")
        else:
            already_follower = True

    # Tweet like form processing
    if request.POST.get("other_profile_tweet_comment_form_submit_btn"):
        current_tweet_id = request.POST.get("hidden_tweet_id")
        return HttpResponseRedirect("/tweet/" + str(current_tweet_id) + "/")

    # Tweet comment form processing
    if request.POST.get("other_profile_tweet_like_form_submit_btn"):
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
        "other_user_profile": other_user_profile,
        "all_tweets": all_tweets,
        "tweet_amount": len(all_tweets),
        "follower_amount": len(all_followers),
        "following_amount": len(all_followings),
        "already_follower": already_follower,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "profile/other_profile.html", data)
