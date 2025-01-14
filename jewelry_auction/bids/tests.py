from django.test import TestCase, Client
from django.urls import reverse
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from users.models import User
from jewelry.models import Jewelry

class BidsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = User.objects.create_user(
            username='owner',
            password='password')
        self.manager = User.objects.create_user(
            username='manager',
            password='password')
        self.user = User.objects.create_user(
            username='user',
            password='password',
            jcoin_balance=2000 
        )
        self.jewelry = Jewelry.objects.create(
            name='Test Jewelry',
            owner=self.owner,
            initial_price=1000,  
            final_price=1000  
        )
        self.auction = Auction.objects.create(
            jewelry=self.jewelry,
            manager=self.manager,
            start_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 10, 0, 0)),
            end_time=timezone.make_aware(timezone.datetime(2025, 1, 1, 12, 0, 0)),
            status='OPEN'  
        )
        self.bid = Bid.objects.create(
            user=self.user,
            auction=self.auction,
            amount=1000
        )

    def test_place_bid_view(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('bids:place_bid', args=[self.auction.pk]))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bids/place_bid.html')

    def test_user_bids_view(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('bids:user_bids'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bids/user_bids.html')
        self.assertEqual(len(response.context['bids']), 1)
