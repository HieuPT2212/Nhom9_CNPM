from django.test import TestCase, Client
from django.urls import reverse
from .models import Jewelry
from users.models import User
from django.utils import timezone

class JewelryViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = User.objects.create_user(
            username='owner',
            password='password',
            role='MEMBER'
        )
        self.manager = User.objects.create_user(
            username='manager',
            password='password',
            role='MANAGER'
        )
        self.user = User.objects.create_user(
            username='user',
            password='password',
            role='MEMBER'
        )
        self.jewelry = Jewelry.objects.create(
            name='Test Jewelry',
            owner=self.owner,
            initial_price=1000,
            status='APPROVED'
        )

    def test_jewelry_create_view_get(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('jewelry:jewelry-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jewelry/jewelry_create.html')

    def test_jewelry_create_view_post(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('jewelry:jewelry-create'), {
            'name': 'New Jewelry',
            'initial_price': 2000,
            'description': 'A beautiful piece of jewelry.'
        })
        if response.status_code != 302:
            print(response.context['form'].errors)  
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Jewelry.objects.filter(name='New Jewelry').exists())

    def test_jewelry_list_view(self):
        response = self.client.get(reverse('jewelry:jewelry-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jewelry/jewelry_list.html')
        self.assertContains(response, 'Test Jewelry')

    def test_jewelry_detail_view(self):
        response = self.client.get(reverse('jewelry:jewelry-detail', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jewelry/jewelry_detail.html')
        self.assertContains(response, 'Test Jewelry')

    def test_jewelry_update_view_get(self):
        self.client.login(username='owner', password='password')
        response = self.client.get(reverse('jewelry:jewelry-update', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jewelry/jewelry_update.html')

    def test_jewelry_update_view_post(self):
        self.client.login(username='owner', password='password')
        response = self.client.post(reverse('jewelry:jewelry-update', args=[self.jewelry.pk]), {
            'name': 'Updated Jewelry',
            'initial_price': 1500,
            'description': 'An updated description for the jewelry.'
        })
        if response.status_code != 302:
            print(response.context['form'].errors)  
        self.assertEqual(response.status_code, 302)  
        self.jewelry.refresh_from_db()
        self.assertEqual(self.jewelry.name, 'Updated Jewelry')
        self.assertEqual(self.jewelry.description, 'An updated description for the jewelry.')

    def test_jewelry_delete_view(self):
        self.client.login(username='owner', password='password')
        response = self.client.post(reverse('jewelry:jewelry-delete', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 302) 
        self.assertFalse(Jewelry.objects.filter(pk=self.jewelry.pk).exists())

    def test_my_jewelry_list_view(self):
        self.client.login(username='owner', password='password')
        response = self.client.get(reverse('jewelry:my_jewelry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jewelry/my_jewelry_list.html')
        self.assertContains(response, 'Test Jewelry')

    def test_jewelry_update_by_staff_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.post(reverse('jewelry:jewelry-update-jewelry-by-staff-or-manager', args=[self.jewelry.pk]), {
            'preliminary_price': 1200,
            'final_price': 1500,
            'received_at': timezone.now()
        })
        self.assertEqual(response.status_code, 302) 
        self.jewelry.refresh_from_db()
        self.assertEqual(self.jewelry.preliminary_price, 1200)
        self.assertEqual(self.jewelry.final_price, 1500)

    def test_jewelry_confirm_auction_view(self):
        self.client.login(username='owner', password='password')
        response = self.client.post(reverse('jewelry:jewelry-confirm-auction', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 302)  
        self.jewelry.refresh_from_db()
        self.assertTrue(self.jewelry.seller_approved)

    def test_jewelry_approve_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.post(reverse('jewelry:jewelry-approve', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 302)  
        self.jewelry.refresh_from_db()
        self.assertEqual(self.jewelry.status, 'APPROVED')

    def test_jewelry_reject_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.post(reverse('jewelry:jewelry-reject', args=[self.jewelry.pk]))
        self.assertEqual(response.status_code, 302)  
        self.jewelry.refresh_from_db()
        self.assertEqual(self.jewelry.status, 'REJECTED')