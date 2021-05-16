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
from .models import Tweet
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

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "home/home.html", data)
