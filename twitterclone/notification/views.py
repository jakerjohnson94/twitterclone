from django.shortcuts import render, redirect, get_object_or_404
from twitterclone.helpers import get_user_data
from .models import Notification


def user_notifications(request):
    html = "user_notifications.html"
    data = get_user_data(request.user)
    return render(request, html, data)


def delete_notification(request, n_id):
    Notification.objects.filter(id=n_id).delete()
    return redirect("/notifications/")
