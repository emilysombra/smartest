from django.test import Client, TestCase
from .models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Course.objects.create(title='Test',
                              description='testing',
                              reference='www.google.com')
    
    def test_course_model(self):
        test_course = Course.objects.get(title='Test')
        self.assertEqual(test_course.description, 'testing')
        self.assertEqual(test_course.reference, 'www.google.com')
        self.assertEqual(str(test_course), 'Test')
    
    def test_get_courses_list(self):
        # testing list
        response = self.client.get("/courses/")
        self.assertEqual(len(response.json()), 1)
        self.assertContains(response, 'Test', count=1)
    
    def test_get_course_item(self):
        # testing item success
        response = self.client.get("/courses/2/")
        self.assertContains(response, 'Test', count=1)
        # testing item not found
        response = self.client.get("/courses/1/")
        self.assertContains(response, 'No Course', status_code=404)
