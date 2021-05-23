from django.urls import path
from . import views

urlpatterns = [
    # Index redirector
    path("", views.index, name="index"),
    # home Page
    path("home/<int:page>/", views.home, name="home"),
    # Single tweet page
    path("tweet/<int:tweet_id>/", views.tweet_single, name="tweet_single"),
]
