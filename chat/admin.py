from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'sender', 'receiver', 'created_at']
    ordering = ['created_at']


admin.site.register(Message, MessageAdmin)
