# DS: TweetComment

This data structure holds the comments of each tweet. You can think of each tweet as its own little world with comments, replies, likes of it's own.

```python
class TweetComment(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    content = models.TextField()
    commentor = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    like_amount = models.IntegerField(default=0)

    def __str__(self):
        return "Comment id: " + str(self.id)
```
