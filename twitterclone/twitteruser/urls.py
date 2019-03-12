from django.contrib import admin
from django.urls import path
from twitterclone.twitteruser.views import user_detail

urlpatterns = [path("user/<int:user_id>", user_detail, name="userdetail")]

