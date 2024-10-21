from rest_framework import viewsets
from .models import Message
from django_filters import rest_framework as filters

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    # serializer_class = MessageSerializer
