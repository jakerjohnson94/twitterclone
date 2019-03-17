from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(
        User, verbose_name="User", on_delete=models.CASCADE, unique=True
    )
    handle = models.CharField("Twitter Handle", max_length=18, unique=True)
    followers = models.ManyToManyField(
        "TwitterUser", verbose_name="Followers", blank=True
    )
    email = models.EmailField("Email", unique=True)

    def __str__(self):
        return self.handle
