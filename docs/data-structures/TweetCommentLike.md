# DS: TweetCommentLike

This data structure holds the likes and likers of each comment (reply) made to a single tweet.

```python
class TweetCommentLike(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    tweet_comment = models.ForeignKey(
        TweetComment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    liker = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return "Like id: " + str(self.id)
```
