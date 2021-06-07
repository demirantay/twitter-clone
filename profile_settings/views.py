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


def settings(request):
    """in this view the users can change their settings"""

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

    # Settings form processing
    empty_input = False

    if request.POST.get("settings_submit_form_btn"):
        profile_photo = request.FILES.get("profile_photo")
        banner_photo = request.FILES.get("banner_photo")
        full_name = request.POST.get("full_name")
        bio = request.POST.get("bio")

        # check if vals are empty if not than update settings
        if bool(profile_photo) == False or bool(banner_photo) == False or \
           bool(full_name) == False or full_name == "" or \
           bool(bio) == False or bio == "":
            empty_input = True
        else:
            current_basic_user_profile.profile_photo = profile_photo
            current_basic_user_profile.banner_photo = banner_photo
            current_basic_user_profile.full_name = full_name
            current_basic_user_profile.bio = bio
            current_basic_user_profile.save()
            return HttpResponseRedirect("/profile/")


    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
    }

    return render(request, "settings/settings.html", data)
