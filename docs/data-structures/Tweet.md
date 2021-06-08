# DS: Tweet

These data structures are the backbone of the application because basically all of tweitter is based on these little tweets

```python
class Tweet(models.Model):
    user = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to="tweet_photo/", blank=True, null=True
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    tweet_like_amount = models.IntegerField(default=0)
    tweet_comment_amount = models.IntegerField(default=0)

    def __str__(self):
        return "Tweet id: " + str(self.id)
```
