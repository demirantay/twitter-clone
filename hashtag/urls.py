from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("explore/", views.explore, name="explore"),
]
