from django.db import models
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import F
from core.models import FeeConfiguration
from bids.models import Bid

class Auction(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('CANCELED', 'Canceled'),
    )

    auction_id = models.AutoField(primary_key=True)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_auctions')
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_auctions')
    sell_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctioned_jewelries', null=True, blank=True) # <---- THÊM TRƯỜNG sell_id
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')
    winning_bid = models.OneToOneField('bids.Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name="won_auction")

    def __str__(self):
        return f"Auction {self.auction_id} for {self.jewelry.name}"

    def is_open(self):
        """Kiểm tra xem phiên đấu giá có đang mở hay không."""
        return self.status == 'OPEN'

    def open_auction(self):
        """Mở phiên đấu giá."""
        if self.status == 'CREATED' and self.start_time <= timezone.now():
            self.status = 'OPEN'
            self.save()

    def close_auction(self):
        from transactions.models import Transaction
        from django.db import transaction as db_transaction
        """Đóng phiên đấu giá, cập nhật bid thắng, trạng thái jewelry, tạo giao dịch, trừ/cộng JCoin."""
        print(f"close_auction method called for Auction ID: {self.pk}, Status: {self.status}, End Time: {self.end_time}, Current Time: {timezone.now()}") # Log - Entry point

        if self.status == 'OPEN' and self.end_time <= timezone.now():
            self.status = 'CLOSED'
            print(f"close_auction: Auction {self.pk} status set to CLOSED.") # Log - Status set to CLOSED
            highest_bid = self.bids.select_related('user').order_by('-amount').first()

            with db_transaction.atomic():
                if highest_bid:
                    self.winning_bid = highest_bid
                    self.save()
                    print(f"close_auction: Auction {self.pk} - Auction object saved after setting winning bid.") # Log - Auction save after winning bid

                    # Cập nhật trạng thái của jewelry
                    auction_jewelry = self.jewelry
                    auction_jewelry.status = 'SOLD'
                    auction_jewelry.owner = highest_bid.user  # Cập nhật owner_id của trang sức
                    auction_jewelry.final_price= highest_bid.amount
                    auction_jewelry.save()
                    print(f"close_auction: Auction {self.pk} - Jewelry status updated and saved for winning bid.") # Log - Jewelry save for winning bid

                    # Tạo Transaction (nếu đấu giá thành công)
                    fee_config = FeeConfiguration.objects.first()
                    if fee_config:
                        transaction_amount = highest_bid.amount
                        fee = transaction_amount * fee_config.fee_rate

                        # Khởi tạo transaction
                        transaction = Transaction.objects.create(
                            auction=self,
                            winning_bidder=highest_bid.user,
                            jewelry_owner=auction_jewelry.owner,
                            amount=transaction_amount,
                            fee=fee,
                            status='COMPLETED'
                        )
                        print(f"close_auction: Auction {self.pk} - Transaction created for winning bid.") # Log - Transaction created

                        # Chuyển JCoin với F expressions và select_for_update()
                        User.objects.filter(pk=highest_bid.user.pk).select_for_update().update(jcoin_balance=F('jcoin_balance') - transaction_amount)
                        User.objects.filter(pk=auction_jewelry.owner.pk).select_for_update().update(jcoin_balance=F('jcoin_balance') + (transaction_amount - fee))
                        print(f"close_auction: Auction {self.pk} - JCoin balance updated for winning bid.") # Log - JCoin updated

                else:
                    # Nếu không có bid nào, cập nhật trạng thái jewelry về 'NO_BIDS'
                    auction_jewelry = self.jewelry
                    print(f"Auction {self.pk}: No bids found.") # Log - No bids
                    auction_jewelry = self.jewelry
                    auction_jewelry.status = 'NO_BIDS'
                    print(f"Auction {self.pk}: Setting jewelry status to NO_BIDS.") # Log - Setting jewelry status to NO_BIDS
                    try:
                        auction_jewelry.save()
                        print(f"Auction {self.pk}: Jewelry status saved successfully.") # Log - Jewelry status saved successfully
                    except Exception as e:
                        print(f"Auction {self.pk}: Error saving jewelry status: {e}") # Log - Error saving jewelry status
                        raise # Vẫn raise lỗi để traceback hiển thị

                    # Tạo Transaction với status 'FAILED' khi không có bid nào
                    transaction = Transaction.objects.create(
                        auction=self,
                        jewelry_owner=auction_jewelry.owner, # Chủ sở hữu trang sức vẫn là người bán ban đầu
                        status='FAILED' # Đặt status là 'FAILED'
                        # Các trường khác như winning_bidder, amount, fee có thể để trống hoặc None tùy thuộc vào model Transaction của bạn
                    )
                    print(f"close_auction: Auction {self.pk} - Transaction created with status FAILED (no bids).") # Log - Transaction FAILED created

                self.save() # <---- THÊM DÒNG NÀY: Lưu đối tượng Auction sau khi đã xử lý xong (cả 2 trường hợp có/không có bid)
                print(f"close_auction: Auction {self.pk} - Auction object saved after processing bids (or no bids).") # Log - Auction save after processing bids
        elif self.status != 'OPEN':
            print(f"close_auction: Auction {self.pk} is not OPEN. Status: {self.status}") # Log - Not open status
            raise ValidationError("Auction is not open.")
        else:
            print(f"close_auction: Auction {self.pk} has not ended yet. End Time: {self.end_time}, Current Time: {timezone.now()}") # Log - Not ended yet
            raise ValidationError("Auction has not ended yet.")
        print(f"close_auction: Method END for Auction ID: {self.pk}") # Log - Method exit

    def save(self, *args, **kwargs):
        # Kiểm tra trạng thái của jewelry trước khi lưu
        if self.pk is None:  # Nếu là tạo mới
            # Cho phép tạo auction nếu jewelry có trạng thái 'APPROVED' hoặc 'NO_BIDS'
            if self.jewelry.status not in ['APPROVED', 'NO_BIDS']:
                raise ValidationError("Cannot create an auction for a jewelry that is not approved.")
        super().save(*args, **kwargs)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be greater than start time.")
        if self.end_time <= timezone.now():
            raise ValidationError("End time must be in the future.")
