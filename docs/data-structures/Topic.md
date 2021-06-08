# DS: Topic

This data structure holds the topic values, these will be used to link to Tweets, explore pages and all kinds of various things that will need a category

```python
class Topic(models.Model):
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Topic: " + str(self.name)

```
