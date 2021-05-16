# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile


def explore(request):
    """aa"""

    data = {}

    return render(request, "hashtag/explore.html", data)


def topic_explore(request, topic):
    """aa"""

    data = {}

    return render(request, "hashtag/topic_explore.html", data)
