from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("notification/", views.notification, name="notification"),
]
