from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    from twitterclone.twitteruser.models import TwitterUser

    body = models.CharField("Body", max_length=50)
    timestamp = timezone.now()
    sender_id = models.ForeignKey(
        TwitterUser, verbose_name="Sender", on_delete=models.CASCADE
    )

    def __str__(self):
        timestamp = self.timestamp
        month = str(timestamp.month)
        day = str(timestamp.day)
        year = str(timestamp.year)
        time = str(timestamp.hour) + ":" + str(timestamp.minute)
        date = f"{month} {day}, {year}, {time}"
        return self.sender_id.handle + " " + date

