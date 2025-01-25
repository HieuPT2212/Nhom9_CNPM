from django.test import TestCase, Client
from django.urls import reverse
from users.models import User

class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_register_view_post(self):
        response = self.client.post(reverse('users:register'), {
        'username': 'newuser',
        'first_name': 'First',
        'last_name': 'Last',
        'password': 'Testpassword123!', 
        'password_confirm': 'Testpassword123!'  
        })
        if response.status_code != 302:
            print("Form errors:", response.context['form'].errors) 
            print("Response content:", response.content.decode())   
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())



    def test_login_view_post(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(response.url.startswith('/'))  

    def test_logout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(response.url.startswith('/'))  

    def test_profile_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')