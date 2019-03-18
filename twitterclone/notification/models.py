from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


class Notification(models.Model):
    tweet = models.ForeignKey(
        Tweet, verbose_name="Tweet", on_delete=models.CASCADE
    )
    tagged = models.ForeignKey(
        TwitterUser, verbose_name="Tagged User", on_delete=models.CASCADE
    )

    def __str__(self):
        time = self.tweet.timestamp.time()
        user_display_name = self.tagged.handle.title()
        sender_name = self.tweet.sender_id.handle.title()
        return (
            f" {time} @{user_display_name} tagged in Tweet from  @{sender_name}"
        )

