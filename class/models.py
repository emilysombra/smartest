from django.db import models


class Class(models.Model):
    class Meta:
        db_table = 'careers'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=64)
    content = models.TextField()
    reference = models.URLField(max_length=200)
