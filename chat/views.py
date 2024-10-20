from rest_framework import viewsets
from .models import Message

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    # serializer_class = MessageSerializer
