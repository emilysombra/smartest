from django.db import models


class Course(models.Model):
    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=64)
    description = models.TextField()
    reference = models.URLField(max_length=200)
