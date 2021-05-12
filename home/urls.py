from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("", views.home, name="home"),
]
