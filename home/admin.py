from django.contrib import admin
from .models import Tweet, TweetComment, TweetRetweet, TweetLike, TweetCommentLike

# Register your models here.
admin.site.register(Tweet)
admin.site.register(TweetComment)
admin.site.register(TweetRetweet)
admin.site.register(TweetLike)
admin.site.register(TweetCommentLike)
