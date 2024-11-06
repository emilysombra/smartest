from rest_framework import viewsets, mixins, status
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
    bot = ChatBot()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMessageSerializer

        return MessageSerializer

    def new_bot_message(self):
        self.bot.get_response("como você está?")
        data = {'receiver': UUID('3352f124-ea31-4c99-b9d1-111d97e4d892'),
                'sender': UUID('e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5'),
                'content': 'generated message'}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        new_serializer = self.new_bot_message()
        headers = self.get_success_headers(new_serializer.data)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
