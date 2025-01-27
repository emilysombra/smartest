from django.db import models

class Message(models.Model):
    '''Stores a single message entity, containing all necessary
    information regarding messages between users and the chatbot.
    The id 'e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5' (both in sender and
    receiver) will always be refering to the chatbot. Otherwise, it will
    be an user.
    '''
    class Meta:
        db_table = 'messages'
        get_latest_by = "created_at"
        ordering = ["created_at"]

    content = models.TextField()
    sender = models.UUIDField()
    receiver = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
