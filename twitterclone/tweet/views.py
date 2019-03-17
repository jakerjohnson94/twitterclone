from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from .forms import PostTweetForm
from twitterclone.helpers import get_user_data


def tweet_detail(request, tweet_id):
    html = "tweet_detail.html"
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, html, {"tweet": tweet})


@login_required
def tweet_post(request):
    data = get_user_data(request.user)["data"]
    print(data)
    html = "tweet_post.html"
    if request.method == "POST":
        form = PostTweetForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender_id = data["user"]
            obj.save()
            # data = form.cleaned_data
            # body = data["body"]

            # twitter_user = get_object_or_404(TwitterUser, user=request.user)
            # Tweet.objects.create(sender_id=twitter_user, body=body)
            return redirect("homepage")

    else:
        form = PostTweetForm()
    return render(request, "tweet_post.html", {"form": form})
