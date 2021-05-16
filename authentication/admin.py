from django.contrib import admin
from .models import BasicUserProfile, Follower

# Register your models here.
admin.site.register(BasicUserProfile)
admin.site.register(Follower)
