# DS: NotificationLike

This data structures holds values such as notifications a notification is basically a "alert" to a single user. For now users only get notified if somebody likes their tweets.

```python
class NotificationLike(models.Model):
    notified = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="notified"
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    notifier = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="notifier"
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Notification id: " + str(self.id)

```
