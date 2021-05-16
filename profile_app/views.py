# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile


def profile(request):
    """aa"""

    data = {}

    return render(request, "profile/profile.html", data)


def other_user_profile(request, other_user_username):
    """aaa"""

    data = {}

    return render(request, "profile/other_user_profile.html", data)
