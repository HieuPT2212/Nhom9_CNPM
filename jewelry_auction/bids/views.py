from django.shortcuts import render, get_object_or_404, redirect
from .models import Bid
from auctions.models import Auction
from .forms import BidForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from notifications.models import Notification

@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    if auction.status != 'OPEN':
        return HttpResponseForbidden("This auction is not open for bidding.")

    if request.method == 'POST':
        form = BidForm(request.POST)
        # Gán user và auction vào form.instance trước khi gọi is_valid()
        form.instance.user = request.user
        form.instance.auction = auction
        if form.is_valid():
            try:
                with transaction.atomic():
                    bid = form.save()
                    return redirect('auctions:auction-detail', pk=auction_id)
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BidForm()

    return render(request, 'bids/place_bid.html', {'form': form, 'auction': auction})

@login_required
def user_bids(request):
    bids = Bid.objects.filter(user=request.user).order_by('-timestamp')
    
    # Pagination
    paginator = Paginator(bids, 10)  # Show 10 bids per page
    page = request.GET.get('page')
    try:
        bids_page = paginator.page(page)
    except PageNotAnInteger:
        bids_page = paginator.page(1)
    except EmptyPage:
        bids_page = paginator.page(paginator.num_pages)
    
    return render(request, 'bids/user_bids.html', {'bids': bids_page})