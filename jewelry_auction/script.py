import os
import django
import random
from django.utils import timezone
from decimal import Decimal

# Thiết lập môi trường Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jewelry_auction.settings")
django.setup()

from users.models import User
from jewelry.models import Jewelry
from auctions.models import Auction
from bids.models import Bid

# Tạo người dùng mẫu
users = []
for i in range(10):
    user = User.objects.create_user(
        username=f'user{i}',
        password='password123',
        jcoin_balance=random.randint(500, 5000)
    )
    users.append(user)

# Tạo trang sức mẫu
jewelries = []
for i in range(10):
    owner = random.choice(users)
    jewelry = Jewelry.objects.create(
        name=f'Jewelry {i}',
        description=f'Description for jewelry {i}',
        owner=owner,
        initial_price=Decimal(random.randint(100, 1000)),
        status='APPROVED',
    )
    jewelries.append(jewelry)

# Tạo đấu giá mẫu
auctions = []
for i in range(5):
    jewelry = random.choice(jewelries)
    auction = Auction.objects.create(
        jewelry=jewelry,
        manager=random.choice(users),
        start_time=timezone.now(),
        end_time=timezone.now() + timezone.timedelta(days=random.randint(1, 5)),
        status='OPEN',
    )
    auctions.append(auction)

# Tạo giá thầu mẫu
for _ in range(20):
    auction = random.choice(auctions)
    user = random.choice(users)
    if user != auction.jewelry.owner:
        bid = Bid.objects.create(
            auction=auction,
            user=user,
            amount=Decimal(random.randint(int(auction.jewelry.initial_price) + 10, int(auction.jewelry.initial_price) + 500)),
        )

print("Sample data generated successfully!")
