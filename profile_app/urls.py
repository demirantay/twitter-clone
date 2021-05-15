from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("profile/", views.profile, name="profile"),
]
