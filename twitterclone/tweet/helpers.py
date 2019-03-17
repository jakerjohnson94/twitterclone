from twitterclone.twitteruser.models import TwitterUser
from django.shortcuts import get_object_or_404


def get_mentioned_user(message):
    user_handles = TwitterUser.objects.values_list("handle", flat=True)
    message_list = message.split(" ")
    for word in message_list:
        if word.startswith("@"):
            if word[1:] in user_handles:
                notified_user = get_object_or_404(TwitterUser, handle=word[1:])
                return notified_user
    return False

