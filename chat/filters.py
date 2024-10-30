from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Message


class MessageFilter(filters.FilterSet):
    user = filters.UUIDFilter(field_name='user', method='filter_user')

    class Meta:
        model = Message
        fields = ['receiver', 'sender']
    
    def filter_user(self, qs, name, value):
        return qs.filter(Q(receiver=value) | Q(sender=value))
