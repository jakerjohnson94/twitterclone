from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tweet(models.Model):
    from twitterclone.twitteruser.models import TwitterUser

    body = models.CharField("Body", max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    sender_id = models.ForeignKey(
        TwitterUser, verbose_name="Sender", on_delete=models.CASCADE
    )
    favorites = models.ManyToManyField(
        TwitterUser,
        related_name="favorites",
        verbose_name="Favorites",
        blank=True,
    )

    def __str__(self):
        timestamp = self.timestamp
        month = str(timestamp.month)
        day = str(timestamp.day)
        year = str(timestamp.year)
        time = f"{str(timestamp.hour)}: {str(timestamp.minute)}"
        date = f"{month} {day}, {year}, {time}"
        return f"{self.sender_id.handle} {date}"
