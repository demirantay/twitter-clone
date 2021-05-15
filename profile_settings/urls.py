from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("settings/", views.settings, name="settings"),
]
