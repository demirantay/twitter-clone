from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("profile/", views.profile, name="profile"),
    path(
        "profile/<str:other_user_username>/",
        views.other_user_profile,
        name="other_user_profile"
    ),
]
