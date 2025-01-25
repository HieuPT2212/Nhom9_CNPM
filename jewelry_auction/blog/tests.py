from django.test import TestCase, Client
from django.urls import reverse
from .models import Blog
from users.models import User
from django.utils import timezone

class BlogViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user',
            password='password',
            role='MEMBER'
        )
        self.manager = User.objects.create_user(
            username='manager',
            password='password',
            role='MANAGER'
        )
        self.admin = User.objects.create_user(
            username='admin',
            password='password',
            role='ADMIN'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='This is a test blog.',
            author=self.user,
            status='APPROVED',
            publication_date=timezone.now()
        )

    def test_blog_create_view_get(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('blog-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_create.html')

    def test_blog_create_view_post(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('blog-create'), {
            'title': 'New Blog',
            'content': 'This is a new blog.'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Blog.objects.filter(title='New Blog').exists())

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertContains(response, 'Test Blog')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog-detail', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        self.assertContains(response, 'Test Blog')

    def test_blog_approve_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('blog-approve', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)  
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.status, 'APPROVED')

    def test_blog_reject_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('blog-reject', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)  
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.status, 'REJECTED')

    def test_blog_pending_list_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('blog-pending-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_pending_list.html')
