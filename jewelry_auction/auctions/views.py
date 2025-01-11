from django.shortcuts import render, get_object_or_404, redirect
from .models import Auction
from .forms import AuctionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def is_manager(user):
    return user.role == 'MANAGER'

@login_required
@user_passes_test(is_manager)
def auction_create(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.manager = request.user
            auction.save()
            return redirect('auctions:auction-list')
    else:
        form = AuctionForm()
    return render(request, 'auctions/auction_create.html', {'form': form})

@login_required
def auction_list(request):
    auction_list = Auction.objects.all()

    # Lọc theo trạng thái nếu user là MANAGER
    if request.user.is_authenticated and request.user.role == 'MANAGER':
        status = request.GET.get('status')
        if status:
            auction_list = auction_list.filter(status=status)
    else:
        auction_list = auction_list.filter(status__in=['OPEN', 'CLOSED'])
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        auction_list = auction_list.filter(
            Q(jewelry__name__icontains=search_query) |
            Q(jewelry__owner__username__icontains=search_query) |
            Q(manager__username__icontains=search_query) |
            Q(staff__username__icontains=search_query)
        )

    # Sort
    sort_by = request.GET.get('sort')
    if sort_by:
        auction_list = auction_list.order_by(sort_by)

    # Pagination
    paginator = Paginator(auction_list, 5)  # Show 5 auctions per page
    page = request.GET.get('page')
    try:
        auctions = paginator.page(page)
    except PageNotAnInteger:
        auctions = paginator.page(1)
    except EmptyPage:
        auctions = paginator.page(paginator.num_pages)
    
    return render(request, 'auctions/auction_list.html', {'auctions': auctions})

def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    return render(request, 'auctions/auction_detail.html', {'auction': auction})

@login_required
@user_passes_test(is_manager)
def auction_update(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    if request.user != auction.manager:
        return HttpResponseForbidden("You don't have permission to edit this auction.")
    if request.method == 'POST':
        form = AuctionForm(request.POST, instance=auction)
        if form.is_valid():
            form.save()
            return redirect('auctions:auction-detail', pk=auction.pk)
    else:
        form = AuctionForm(instance=auction)
    return render(request, 'auctions/auction_update.html', {'form': form})

@login_required
@user_passes_test(is_manager)
def auction_delete(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    if request.user != auction.manager:
        return HttpResponseForbidden("You don't have permission to delete this auction.")
    if request.method == 'POST':
        auction.delete()
        return redirect('auctions:auction-list')
    return render(request, 'auctions/auction_delete.html', {'auction': auction})

@login_required
@user_passes_test(is_manager)
def auction_cancel(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    if request.user != auction.manager:
        return HttpResponseForbidden("You don't have permission to cancel this auction.")
    if request.method == 'POST':
        if auction.status == 'CREATED':
            auction.status = 'CANCELED'
            auction.save()
            return redirect('auctions:auction-list')
        else:
            # Xử lý trường hợp auction không ở trạng thái CREATED
            return redirect('auctions:auction-detail', pk=auction.pk)
    return render(request, 'auctions/auction_cancel.html', {'auction': auction})