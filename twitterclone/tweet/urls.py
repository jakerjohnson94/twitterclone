from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import tweet_detail, tweet_post

urlpatterns = [
    path("tweet/<int:tweet_id>", tweet_detail, name="tweetdetail"),
    path("tweet/post", tweet_post, name="tweetpost"),
]

