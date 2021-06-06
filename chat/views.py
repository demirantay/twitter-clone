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
from hashtag.models import Topic
from .models import Chat

from utils.session_utils import get_current_user, get_current_user_profile
from utils.base_utils import left_nav_tweet_form_processing
from utils.base_utils import mobile_tweet_form_processing
from utils.base_utils import get_who_to_follow
from utils.base_utils import get_topics_to_follow


def chat_landing(request):
    """ this is the page that welcomes users to the chat feature """

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

    # Get the current followings
    try:
        current_followings = Follower.objects.filter(
            follower=current_basic_user_profile
        )
    except ObjectDoesNotExist:
        current_followings = None

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "current_followings": current_followings,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "chat/landing.html", data)


def chat_single(request, username):
    """ in this page users can chat with each other """

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

    # Get the current followings
    try:
        current_followings = Follower.objects.filter(
            follower=current_basic_user_profile
        )
    except ObjectDoesNotExist:
        current_followings = None

    # Get the current text reciever (user)
    try:
        current_reciever_user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        current_reciever_user = None

    try:
        current_reciever = BasicUserProfile.objects.get(
            user=current_reciever_user
        )
    except ObjectDoesNotExist:
        current_reciever = None

    if current_reciever_user == None:
        return HttpResponseRedirect("/")

    # Getting the chat history feed
    chat_history_feed = []

    try:
        chat_records_self = Chat.objects.filter(
            sender=current_basic_user_profile,
            reciever=current_reciever
        )
        chat_records_reciever = Chat.objects.filter(
            sender=current_reciever,
            reciever=current_basic_user_profile,
        )
    except ObjectDoesNotExist:
        chat_records_self = None
        chat_records_reciever= None

    print(chat_records_self)

    # Chat text from processing
    if request.POST.get("chat_send_submit_btn"):
        chat_content = request.POST.get("chat_content")
        new_message = Chat(
            content=chat_content,
            sender=current_basic_user_profile,
            reciever=current_reciever,
        )
        new_message.save()
        return HttpResponseRedirect("/chat/"+current_reciever_user.username+"/")

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "who_to_follow": who_to_follow,
        "topics_to_follow": topics_to_follow,
        "current_followings": current_followings,
        "current_reciever": current_reciever,
    }

    if current_basic_user == None:
        return HttpResponseRedirect("/auth/signup/")
    else:
        return render(request, "chat/single.html", data)
