### DS: BaseUserProfile

This model holds the base user profiles. What does that mean? It means that anything that is realted to the basic users which will not be stored in the main `User` model provided by Django will go into `BaseUserProfile` such as profile photo, banner photo, full name, bio ... etc.

```python

class BasicUserProfile(models.Model):
    # O2One relationship with django's user model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    # Edit Profile -- settings
    profile_photo = models.ImageField(
        upload_to="profile_photo/", blank=True, null=True
    )
    banner_photo = models.ImageField(
        upload_to="banner_photo/", blank=True, null=True
    )
    email = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return "User: " + str(self.user.username)

```
