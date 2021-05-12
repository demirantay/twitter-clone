# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports


def home(request):
    """this is the homepage of the site and is an proxy redirector"""

    # admin user session pop
    # admin user session pop
    # Deleting any sessions regarding top-tier type of users


    data = {}
    return render(request, "home/home.html", data)
