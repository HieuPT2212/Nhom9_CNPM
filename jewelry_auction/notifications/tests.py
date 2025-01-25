from django.test import TestCase, Client
from django.urls import reverse
from .models import Notification
from users.models import User

class NotificationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = User.objects.create_user(
            username='user',
            password='password',
            role='MEMBER',
        )
        self.notification = Notification.objects.create(
            user=self.owner,
            message='This is a message',
            is_read=False,
        )

    def test_notification_list(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('notifications:notification-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notifications/notification_list.html')
        self.assertContains(response, 'This is a message')

    def test_notification_detail(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('notifications:notification-detail', args=[self.notification.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notifications/notification_detail.html')
        self.assertContains(response, 'This is a message')
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)