from twitterclone.twitteruser.models import TwitterUser
from django.utils.html import format_html, html_safe
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render


def get_mentioned_users(message):
    user_handles = TwitterUser.objects.values_list("handle", flat=True)
    message_list = message.split(" ")
    notified_users = []
    new_message = []
    for word in message_list:

        if word.startswith("@") and word[1:] in user_handles:
            notified_user = get_object_or_404(TwitterUser, handle=word[1:])
            notified_users.append(notified_user)

            new_word = format_html(
                '<a href="{}">@{}</a>',
                reverse_lazy("userdetail", args=[notified_user.id]),
                notified_user.handle,
            )

            new_message.append(new_word)

        else:
            new_message.append(word)

    new_message = " ".join(new_message)
    if len(notified_users) >= 1:
        return (notified_users, new_message)
    else:
        return (None, new_message)


def format_body_with_mention(body):
    user_handles = TwitterUser.objects.values_list("handle", flat=True)
    message_list = message.split(" ")
    for word in message_list:
        if word.startswith("@"):
            if word[1:] in user_handles:
                notified_user = get_object_or_404(TwitterUser, handle=word[1:])
                return notified_user
    return False
