from django.test import TestCase, Client
from blog.models import Blog
from jewelry.models import Jewelry
from notifications.models import Notification
from users.models import User
# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.blog = Blog.objects.create(blog_id =1,title='Test Blog', content='This is a test blog.', author=self.user)
        self.jewelry = Jewelry.objects.create(jewelry_id=1, name='Test Jewelry', description='This is a test jewelry.', owner=self.user, initial_price = 1000)
        self.notification = Notification.objects.create(user=self.user, message='This is a test notification.')

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
