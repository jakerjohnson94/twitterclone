from django.contrib import admin
from django.urls import path
from twitterclone.twitteruser.views import (
    user_detail,
    user_homepage,
    user_signup,
    user_info_page,
    user_follow,
    user_unfollow,
    user_list,
    user_followers,
    user_following,
)

urlpatterns = [
    path("", user_homepage, name="homepage"),
    path("signup/", user_signup, name="signup"),
    path("user/<int:user_id>", user_info_page, name="userdetail"),
    path("user/followers/<int:user_id>", user_followers, name="followers"),
    path("user/following/<int:user_id>", user_following, name="following"),
    path("user/follow/<int:user_id>", user_follow, name="follow"),
    path("user/unfollow/<int:user_id>", user_unfollow, name="unfollow"),
    path("users", user_list, name="userlist"),
]

