# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports
from authentication.models import BasicUserProfile
from home.models import Tweet


# Notification Like
# ---------------
class NotificationLike(models.Model):
    notified = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="notified"
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    notifier = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="notifier"
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Notification id: " + str(self.id)
