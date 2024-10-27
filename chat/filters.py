from django_filters import rest_framework as filters
from .models import Message


class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = ['receiver', 'sender']
