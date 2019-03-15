from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import TwitterUser
from django.contrib.auth.models import User
from .forms import TwitterUserSignupForm
from twitterclone.tweet.models import Tweet


def user_signup(request):
    if request.method == "POST":
        form = TwitterUserSignupForm(request.POST)
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            username = data["handle"]
            raw_password = data["password"]
            email = data["email"]

            user = User.objects.create_user(
                username=username, email=email, password=raw_password
            )
            twitter_user = TwitterUser.objects.create(
                user=user, handle=username, email=email
            )
            login(request, user)
            return redirect("homepage")

    else:
        form = TwitterUserSignupForm()
    return render(request, "user_signup.html", {"form": form})


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


@login_required
def user_homepage(request):
    print(request.user.id)
    html = "user_detail.html"
    twitter_user = get_object_or_404(TwitterUser, user__pk=request.user.id)
    followers = twitter_user.followers.all()
    tweets = Tweet.objects.filter(sender_id=twitter_user.id)
    return render(
        request,
        html,
        {
            "user": twitter_user,
            "followers": followers,
            "follower_cnt": len(followers),
            "tweets": tweets,
        },
    )
