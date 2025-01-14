from django.test import TestCase, Client
from blog.models import Blog
from jewelry.models import Jewelry
from notifications.models import Notification
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = 'core/index.html'
        self.about_url = 'core/about.html'
        self.policy_url = 'core/policy.html'
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.home_url)
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.about_url)
    def test_policy(self):
        response = self.client.get('/policy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.policy_url)
