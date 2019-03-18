from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Tweet
from .forms import PostTweetForm
from twitterclone.helpers import get_user_data
from twitterclone.tweet.helpers import get_mentioned_users
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser


def tweet_detail(request, tweet_id):
    html = "tweet_detail_view.html"
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    user = request.user.twitter_user
    return render(request, html, {"tweet": tweet, "user": user})


@login_required
def tweet_post(request):
    user_data = get_user_data(request.user)
    html = "tweet_post.html"
    if request.method == "POST":
        form = PostTweetForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            body = form_data["body"]
            sender = user_data["user"]
            mentioned_users, new_body = get_mentioned_users(body)
            tweet = Tweet.objects.create(sender_id=sender, body=new_body)

            if mentioned_users is not None:
                for mentioned_user in mentioned_users:
                    Notification.objects.create(
                        tweet=tweet, tagged=mentioned_user
                    )

            return redirect("homepage")

    else:
        form = PostTweetForm()
    return render(request, "tweet_post.html", {"form": form})


def tweet_delete(request, tweet_id):
    user = request.user.twitteruser
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    tweet.delete()
    return redirect(request.GET.get("next", "/"))
