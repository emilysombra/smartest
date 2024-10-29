from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Message
from .serializers import MessageSerializer
from .filters import MessageFilter


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = MessageSerializer
    filterset_class = MessageFilter