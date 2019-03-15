from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from twitterclone.forms import LoginForm


def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_action(request):
    html = "logout.html"
    logout(request)
    return redirect(request.GET.get("next", "/"))
