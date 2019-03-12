from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Tweet


def tweet_detail(request, tweet_id):
    html = "tweet_detail.html"
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, html, {"tweet": tweet})

