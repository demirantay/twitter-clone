from django.urls import path
from . import views

urlpatterns = [
    # home Page
    path("search/<str:query>/", views.search, name="search"),
]
