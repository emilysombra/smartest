from django.test import TestCase, Client
from .models import Career


class CareerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Career.objects.create(title='Test Career',
                              description='testing',
                              reference='www.youtube.com')
    
    def test_career_model(self):
        test_career = Career.objects.get(title='Test Career')
        self.assertEqual(test_career.description, 'testing')
        self.assertEqual(test_career.reference, 'www.youtube.com')
    
    def test_get_careers_list(self):
        # testing list
        response = self.client.get("/careers/")
        self.assertEqual(len(response.json()), 1)
        self.assertContains(response, 'Test Career', count=1)
    
    def test_get_career_item(self):
        # testing item success
        response = self.client.get("/careers/2/")
        self.assertContains(response, 'Test Career', count=1)
        # testing item not found
        response = self.client.get("/careers/1/")
        self.assertContains(response, 'No Career', status_code=404)
