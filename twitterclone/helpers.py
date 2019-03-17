from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from itertools import chain


def get_user_data(user):
    auth_user = user
    t_user = get_object_or_404(TwitterUser, user__pk=user.id)
    followers = t_user.followers.all()
    following = TwitterUser.objects.filter(followers=t_user)
    sent_tweets = Tweet.objects.filter(Q(sender_id=t_user.id)).order_by(
        "-timestamp"
    )
    subscribed_tweets = Tweet.objects.filter(
        Q(sender_id__in=following)
    ).order_by("-timestamp")
    # all_tweets = list(chain(sent_tweets, subscribed_tweets)).order_by("timestamp")
    all_tweets = Tweet.objects.filter(
        Q(sender_id=t_user.id) | Q(sender_id__in=following)
    ).order_by("-timestamp")

    return {
        "data": {
            "user": t_user,
            "auth_user": auth_user,
            "followers": followers,
            "following": following,
            "sent_tweets": sent_tweets,
            "subscribed_tweets": subscribed_tweets,
            "tweets": all_tweets,
        }
    }