from django.test import TestCase, Client
from django.urls import reverse
from .models import Transaction
from auctions.models import Auction
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone

class TransactionViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_user(
            username='admin',
            password='password',
            role='ADMIN'
        )
        self.user1 = User.objects.create_user(
            username='user1',
            password='password',
            role='MEMBER'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password',
            role='MEMBER'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            password='password',
            role='MEMBER'
        )
        self.jewelry = Jewelry.objects.create(
            name='Test Jewelry',
            owner=self.user2,
            initial_price=1000,
            status='APPROVED'
        )
        self.auction = Auction.objects.create(
            jewelry=self.jewelry,
            manager=self.admin,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            status='OPEN'
        )
        self.transaction = Transaction.objects.create(
            auction=self.auction,
            winning_bidder=self.user1,
            jewelry_owner=self.user2,
            amount=1000,
            timestamp=timezone.now()
        )

    def test_transaction_list_view_as_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('transactions:transaction-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/transaction_list.html')
        self.assertContains(response, 'Transaction')

    def test_transaction_list_view_as_member(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('transactions:transaction-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/transaction_list.html')
        self.assertContains(response, 'Transaction')

    def test_transaction_detail_view_as_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('transactions:transaction-detail', args=[self.transaction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/transaction_detail.html')
        self.assertContains(response, 'Transaction')

    def test_transaction_detail_view_as_winning_bidder(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('transactions:transaction-detail', args=[self.transaction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/transaction_detail.html')
        self.assertContains(response, 'Transaction')

    def test_transaction_detail_view_as_jewelry_owner(self):
        self.client.login(username='user2', password='password')
        response = self.client.get(reverse('transactions:transaction-detail', args=[self.transaction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/transaction_detail.html')
        self.assertContains(response, 'Transaction')

    def test_transaction_detail_view_forbidden(self):
        self.client.login(username='user3', password='password')
        response = self.client.get(reverse('transactions:transaction-detail', args=[self.transaction.pk]))
        self.assertEqual(response.status_code, 403)  # Forbidden
