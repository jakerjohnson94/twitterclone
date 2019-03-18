from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import tweet_detail, tweet_post, tweet_delete

urlpatterns = [
    path("tweet/<int:tweet_id>", tweet_detail, name="tweetdetail"),
    path("tweet/post", tweet_post, name="tweetpost"),
    path("tweet/delete/<int:tweet_id>", tweet_delete, name="tweetdelete"),
]

