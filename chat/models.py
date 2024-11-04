from django.db import models

class Message(models.Model):
    class Meta:
        db_table = 'messages'
        get_latest_by = "created_at"
        ordering = ["created_at"]

    content = models.TextField()
    sender = models.UUIDField()
    receiver = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
