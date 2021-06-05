from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("explore/", views.explore, name="explore"),
    path("explore/<str:topic>/<int:page>/", views.topic_explore, name="topic_explore"),
]
