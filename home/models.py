# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports
from authentication.models import BasicUserProfile


# Tweet Model
# --------------
# This model holdes the records of tweets made by users
class Tweet(models.Model):
    user = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to="tweet_photo/", blank=True, null=True
    )

    def __str__(self):
        return "Tweet id: " + str(self.id)
