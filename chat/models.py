from django.db import models

class Message(models.Model):
    content = models.TextField()
    sender = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
