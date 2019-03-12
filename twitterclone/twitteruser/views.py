from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import TwitterUser
from twitterclone.tweet.models import Tweet


def user_detail(request, user_id):
    html = "user_detail.html"
    user = get_object_or_404(TwitterUser, pk=user_id)
    followers = user.followers.all()
    tweets = Tweet.objects.filter(sender_id=user_id)
    return render(
        request,
        html,
        {
            "user": user,
            "followers": followers,
            "follower_cnt": len(followers),
            "tweets": tweets,
        },
    )

