from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("chat/landing/", views.chat_landing, name="chat_landing"),
    path("chat/<str:username>/", views.chat_single, name="chat_single"),
]
