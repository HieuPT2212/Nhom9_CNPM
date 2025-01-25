from django.test import TestCase, Client
from django.urls import reverse
from .models import Auction
from users.models import User  
from jewelry.models import Jewelry  
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class AuctionViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.manager = User.objects.create_user(username='manager', password='password', role='MANAGER')
        self.owner = User.objects.create_user(username='owner', password='password', role='MEMBER')
        self.jewelry = Jewelry.objects.create(name='Test Jewelry', owner=self.owner, initial_price=1000)

        self.auction = Auction.objects.create(
            jewelry=self.jewelry,
            manager=self.manager,
            start_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 10, 0, 0)),
            end_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)),
            status='CREATED'
        )

        for i in range(10):
            Auction.objects.create(
                jewelry=self.jewelry,
                manager=self.manager,
                start_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 10, 0, 0)),
                end_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)),
                status='CREATED'
            )

    def test_auction_create_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.get(reverse('auctions:auction-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_create.html')

    def test_auction_list_view(self):
        self.client.login(username='manager', password='password')  
        response = self.client.get(reverse('auctions:auction-list'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_list.html')

    def test_auction_detail_view(self):
        self.client.login(username='manager', password='password')  
        response = self.client.get(reverse('auctions:auction-detail', args=[self.auction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_detail.html')

    def test_auction_update_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.get(reverse('auctions:auction-update', args=[self.auction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_update.html')

    def test_auction_delete_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.get(reverse('auctions:auction-delete', args=[self.auction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_delete.html')

    def test_auction_cancel_view(self):
        self.client.login(username='manager', password='password')
        response = self.client.get(reverse('auctions:auction-cancel', args=[self.auction.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions/auction_cancel.html')
