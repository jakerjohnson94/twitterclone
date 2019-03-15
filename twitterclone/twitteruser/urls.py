from django.contrib import admin
from django.urls import path
from twitterclone.twitteruser.views import (
    user_detail,
    user_homepage,
    user_signup,
)

urlpatterns = [
    path("", user_homepage, name="homepage"),
    path("user/<int:user_id>", user_detail, name="userdetail"),
    path("signup/", user_signup, name="signup"),
]

