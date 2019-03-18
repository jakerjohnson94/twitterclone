from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.notification.models import Notification
from itertools import chain


def get_user_data(user):
    auth_user = user
    t_user = user.twitteruser
    followers = t_user.followers.all()
    following = TwitterUser.objects.filter(followers=t_user)
    sent_tweets = Tweet.objects.filter(sender_id=t_user.id).order_by(
        "-timestamp"
    )
    monitored_tweets = Tweet.objects.filter(sender_id__in=following).order_by(
        "-timestamp"
    )
    all_tweets = (sent_tweets | monitored_tweets).order_by("-timestamp")

    notifications = Notification.objects.filter(tagged=t_user).order_by(
        "-tweet__timestamp"
    )
    favorites = Tweet.objects.filter(favorites=t_user).order_by("-timestamp")
    return {
        "user": t_user,
        "auth_user": auth_user,
        "followers": followers,
        "following": following,
        "sent_tweets": sent_tweets,
        "all_tweets": all_tweets,
        "notifications": notifications,
        "favorites": favorites,
    }
