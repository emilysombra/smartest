from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'sender', 'created_at')


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', 'receiver', 'sender')
