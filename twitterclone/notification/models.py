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
        return f"@{self.tagged.handle.title()} tagged in Tweet from  @{self.tweet.sender_id.handle.title()}"

