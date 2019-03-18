from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    get_list_or_404,
)
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from .models import TwitterUser
from django.contrib.auth.models import User
from .forms import TwitterUserSignupForm
from twitterclone.tweet.models import Tweet
from twitterclone.helpers import get_user_data
import pprint


def user_signup(request):
    if request.method == "POST":
        form = TwitterUserSignupForm(request.POST)
        if form.is_valid():
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
    user = get_object_or_404(User, pk=user_id)
    data = get_user_data(user)
    return render(request, html, data)


def user_info_page(request, user_id):
    html = "user_info_page.html"
    user = get_object_or_404(User, pk=user_id)
    other_user = get_user_data(user)["data"]
    logged_user = get_user_data(request.user)["data"]
    followed = False
    if logged_user["user"] in other_user["followers"].all():
        followed = True
    pprint.pprint(f"logged: {logged_user}             other:{other_user}")
    data = {
        "data": {
            "other_user": other_user,
            "logged_user": logged_user,
            "followed": followed,
        }
    }
    return render(request, html, data)


@login_required
def user_list(request):
    html = "user_list.html"
    users = get_list_or_404(TwitterUser)
    return render(request, html, {"users": users})


@login_required
def user_homepage(request):
    data = get_user_data(request.user)
    html = "user_homepage.html"
    return render(request, html, data)


def user_follow(request, user_id):
    logged_user = get_user_data(request.user)["data"]["user"]
    other_user = get_object_or_404(TwitterUser, pk=user_id)
    other_user.followers.add(logged_user)
    return redirect("homepage")


def user_unfollow(request, user_id):
    logged_user = get_user_data(request.user)["data"]["user"]
    other_user = get_object_or_404(TwitterUser, pk=user_id)
    other_user.followers.remove(logged_user)
    return redirect("homepage")


def user_followers(request, user_id):
    html = "user_list.html"
    user_q = get_object_or_404(User, pk=user_id)
    user = get_user_data(user_q)["data"]["user"]
    followers = user.followers.all()
    return render(
        request,
        html,
        {"title": f"@{user.handle}'s Followers", "users": followers},
    )
