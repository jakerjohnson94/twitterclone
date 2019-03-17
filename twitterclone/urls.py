from django.contrib import admin
from django.urls import path
from twitterclone.notification.models import Notification
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser

from twitterclone.tweet.urls import urlpatterns as tweet_urls
from twitterclone.twitteruser.urls import urlpatterns as user_urls
from twitterclone.notification.urls import urlpatterns as notification_urls
from twitterclone.views import login_view, logout_action

admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(Notification)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_view, name="login"),
    path("logout/", logout_action, name="logout"),
]

urlpatterns += tweet_urls

urlpatterns += user_urls

urlpatterns += notification_urls
