from django.test import TestCase
from .models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(title='Test',
                              description='testing',
                              reference='www.google.com')
    
    def test_course(self):
        test_course = Course.objects.get(title='Test')
        self.assertEqual(test_course.description, 'testing')
        self.assertEqual(test_course.reference, 'www.google.com')
