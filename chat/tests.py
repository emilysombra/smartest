from django.test import Client, TestCase
from uuid import UUID
from .models import Message


class MessageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Message.objects.create(content='message content',
                               sender=UUID('e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5'),
                               receiver=UUID('e7d81ed8-a59c-9cd3-40b3-3ed8fb6c53d3'))
    
    def test_message_model(self):
        test_msg = Message.objects.get(content='message content')
        self.assertEqual(test_msg.sender, UUID('e7d81ea5-d89c-40b3-9cd3-3ed8fb6c53d5'))
        self.assertEqual(test_msg.receiver, UUID('e7d81ed8-a59c-9cd3-40b3-3ed8fb6c53d3'))
    
    def test_get_messages_list(self):
        # testing list
        response = self.client.get("/messages/")
        self.assertEqual(len(response.json()), 1)
        self.assertContains(response, 'message content', count=1)
