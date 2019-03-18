from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    get_list_or_404,
)
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import TwitterUser
from django.contrib.auth.models import User
from .forms import TwitterUserSignupForm
from twitterclone.tweet.models import Tweet
from twitterclone.helpers import get_user_data


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
    other_user = get_user_data(user)
    logged_user = get_user_data(request.user)
    followed = False
    if logged_user["user"] in other_user["followers"].all():
        followed = True
    data = {
        "other_user": other_user,
        "logged_user": logged_user,
        "followed": followed,
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
    logged_user = get_user_data(request.user)["user"]
    other_user = get_object_or_404(TwitterUser, pk=user_id)
    other_user.followers.add(logged_user)
    user_id = other_user.id
    return redirect("userdetail", user_id=user_id)


def user_unfollow(request, user_id):
    logged_user = get_user_data(request.user)["user"]
    other_user = get_object_or_404(TwitterUser, pk=user_id)
    other_user.followers.remove(logged_user)
    user_id = other_user.id
    return redirect("userdetail", user_id=user_id)


def user_followers(request, user_id):
    html = "user_list.html"
    user_q = get_object_or_404(User, pk=user_id)
    user = get_user_data(user_q)["user"]
    followers = user.followers.all()
    return render(
        request,
        html,
        {"title": f"@{user.handle}'s followers", "users": followers},
    )


def user_following(request, user_id):
    html = "user_list.html"
    user_q = get_object_or_404(User, pk=user_id)
    data = get_user_data(user_q)
    user = data["user"]
    following = data["following"]
    return render(
        request,
        html,
        {"title": f"@{user.handle}'s followed users", "users": following},
    )
