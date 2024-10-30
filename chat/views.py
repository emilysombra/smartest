from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Message
from .serializers import MessageSerializer
from .filters import MessageFilter


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Message.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = MessageSerializer
    filterset_class = MessageFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
