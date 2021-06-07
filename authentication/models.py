# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports


# Basic User Profile
# -------------
# This model holds the basis user profile such as email, username .. etc
# more complicated settigns such as privacy, sms ... etc. Basic profile is
# used and created for basic users.
class BasicUserProfile(models.Model):
    # O2One relationship with django's user model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    # Edit Profile -- settings
    profile_photo = models.ImageField(
        upload_to="profile_photo/", blank=True, null=True
    )
    banner_photo = models.ImageField(
        upload_to="banner_photo/", blank=True, null=True
    )
    email = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return "User: " + str(self.user.username)


# Follower
# ----------
# This model holds the follwers of Baseic user profiles
class Follower(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    following = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="following"
    )
    follower = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="follower"
    )

    def __str__(self):
        return "Following: " + str(self.following.user.username) + \
                " | Follower: " + str(self.follower.user.username)
