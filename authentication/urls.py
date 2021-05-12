from django.urls import path
from . import views

urlpatterns = [
    # signup Page
    path("auth/signup/", views.signup, name="signup"),

]
