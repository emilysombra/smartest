from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from uuid import UUID
from .models import Message

User = get_user_model()
USER = 'e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5'


class MessageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username=USER, password='password123')
        Message.objects.create(content='message content',
                               sender=UUID(USER),
                               receiver=UUID('e7d81ed8-a59c-9cd3-40b3-3ed8fb6c53d3'))
    
    def test_message_model(self):
        test_msg = Message.objects.get(content='message content')
        self.assertEqual(test_msg.sender, UUID(USER))
        self.assertEqual(test_msg.receiver, UUID('e7d81ed8-a59c-9cd3-40b3-3ed8fb6c53d3'))
    
    def test_get_messages_list(self):
        # testing list
        response = self.client.get("/messages/")
        self.assertEqual(len(response.json()), 1)
        self.assertContains(response, 'message content', count=1)
    
    def test_filter_messages(self):
        response = self.client.get(f"/messages/?user={USER}")
        self.assertEqual(len(response.json()), 1)
        self.assertContains(response, 'message content', count=1)
    
    def test_create_message(self):
        data = {"content": 'message from API',
                "sender": USER,
                "receiver": 'e7d81ed8-a59c-9cd3-40b3-3ed8fb6c53d3'}
        response = self.client.post("/messages/", data=data)
        self.assertEqual(response.status_code, 401)
