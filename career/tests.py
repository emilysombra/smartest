from django.test import TestCase
from .models import Career


class CareerTestCase(TestCase):
    def setUp(self):
        Career.objects.create(title='Test Career',
                              description='testing',
                              reference='www.youtube.com')
    
    def test_career(self):
        test_career = Career.objects.get(title='Test Career')
        self.assertEqual(test_career.description, 'testing')
        self.assertEqual(test_career.reference, 'www.youtube.com')
