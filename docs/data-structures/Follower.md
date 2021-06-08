# DS: Follower

This model holds all of the following and follower users of the site. It only
cares about basic users with BaseUserProfile's

```python
class Follower(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    following = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="following"
    )
    follower = models.ForeignKey(
        BasicUserProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="follower"
    )

    def __str__(self):
        return "Following: " + str(self.following.user.username) + \
                " | Follower: " + str(self.follower.user.username)
```
