from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    from twitterclone.twitteruser.models import TwitterUser

    body = models.CharField("Body", max_length=50)
    timestamp = timezone.now()
    sender = models.ForeignKey(
        TwitterUser, verbose_name="Sender", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.sender.handle + " " + str(self.timestamp)

