from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
from uuid import UUID
from .models import Message
from .serializers import CreateMessageSerializer, MessageSerializer
from .filters import MessageFilter
from .chatbot import ChatBot


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Message.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = MessageSerializer
    filterset_class = MessageFilter
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMessageSerializer

        return MessageSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        return [permission() for permission in self.permission_classes]

    def new_bot_message(self, receiver, content):
        bot = ChatBot()
        data = {'receiver': UUID(receiver),
                'sender': UUID('e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5'),
                'content': bot.get_response(content)}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        new_serializer = self.new_bot_message(request.data['sender'], request.data['content'])
        headers = self.get_success_headers(new_serializer.data)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
