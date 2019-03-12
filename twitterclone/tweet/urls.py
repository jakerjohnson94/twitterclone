from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import tweet_detail

urlpatterns = [path("tweet/<int:tweet_id>", tweet_detail, name="tweetdetail")]

