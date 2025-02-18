from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Auction

scheduler = BackgroundScheduler()

def open_auctions():
    """Mở các phiên đấu giá đã đến giờ bắt đầu."""
    now = timezone.now()
    auctions_to_open = Auction.objects.filter(status='CREATED', start_time__lte=now)
    for auction in auctions_to_open:
        auction.open_auction()
        print(f"Auction {auction.pk} opened.")

def close_auctions():
    """Đóng các phiên đấu giá đã kết thúc."""
    now = timezone.now()
    auctions_to_close = Auction.objects.filter(status='OPEN', end_time__lte=now)
    for auction in auctions_to_close:
        print(f"close_auctions: Processing auction ID: {auction.pk}, type: {type(auction)}") # Thêm log này
        auction.close_auction() # Dòng có vấn đề (theo traceback cũ)
        print(f"Auction {auction.pk} closed.")

def start_scheduler():
    """Bắt đầu lên lịch các tác vụ."""
    if not scheduler.running:
        scheduler.add_job(open_auctions, 'interval', seconds=1)  # Kiểm tra mỗi phút để mở phiên đấu giá
        scheduler.add_job(close_auctions, 'interval', seconds=1)  # Kiểm tra mỗi phút để đóng phiên đấu giá
        scheduler.start()
        print("Scheduler started.")