# DS: TweetLike

These data structures holds the likes of tweets and which profile liked the tweet so it is easier to sort out who is establishing a connection with eachother.

```python
class TweetLike(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    tweet = models.ForeignKey(
        Tweet,
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
