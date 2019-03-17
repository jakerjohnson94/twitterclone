from django.contrib import admin
from django.urls import path
from .views import user_notifications, delete_notification

urlpatterns = [
    path("notifications/", user_notifications, name="notifications"),
    path(
        "notification/delete/<int:n_id>/",
        delete_notification,
        name="deletenotification",
    ),
]

