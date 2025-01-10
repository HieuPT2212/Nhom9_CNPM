from django.shortcuts import render, get_object_or_404, redirect
from .models import Jewelry
from .forms import JewelryForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def jewelry_create(request):
    if request.method == 'POST':
        form = JewelryForm(request.POST, request.FILES)
        if form.is_valid():
            jewelry = form.save(commit=False)
            jewelry.owner = request.user
            jewelry.save()
            return redirect('jewelry:my_jewelry')
    else:
        form = JewelryForm()
    return render(request, 'jewelry/jewelry_create.html', {'form': form})

def jewelry_list(request):
    jewelry_list = Jewelry.objects.filter(status__in=['APPROVED', 'AUCTIONING', 'NO_BIDS']).order_by('-jewelry_id')
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        jewelry_list = jewelry_list.filter(name__icontains=search_query)

    # Sort
    sort_by = request.GET.get('sort')
    if sort_by:
        jewelry_list = jewelry_list.order_by(sort_by)

    # Pagination
    paginator = Paginator(jewelry_list, 5)  # Show 5 jewelry items per page
    page = request.GET.get('page')
    try:
        jewelries = paginator.page(page)
    except PageNotAnInteger:
        jewelries = paginator.page(1)
    except EmptyPage:
        jewelries = paginator.page(paginator.num_pages)
    
    return render(request, 'jewelry/jewelry_list.html', {'jewelries': jewelries})

def jewelry_detail(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    return render(request, 'jewelry/jewelry_detail.html', {'jewelry': jewelry})

@login_required
def jewelry_update(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    
    if request.user != jewelry.owner and request.user.role not in ['STAFF', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to edit this jewelry.")
    
    if request.method == 'POST':
        form = JewelryForm(request.POST, request.FILES, instance=jewelry)
        if form.is_valid():
            form.save()
            return redirect('jewelry:jewelry-detail', pk=jewelry.pk)
    else:
        form = JewelryForm(instance=jewelry)
    return render(request, 'jewelry/jewelry_update.html', {'form': form, 'jewelry': jewelry})

@login_required
def jewelry_delete(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    if request.user != jewelry.owner:
        return HttpResponseForbidden("You don't have permission to delete this jewelry.")
    if request.method == 'POST':
        jewelry.delete()
        return redirect('jewelry:jewelry-list')
    return render(request, 'jewelry/jewelry_delete.html', {'jewelry': jewelry})

@login_required
def my_jewelry_list(request):
    user = request.user
    if user.is_staff:
        if user.groups.filter(name='Manager').exists() or user.is_superuser:
jewelry_list = Jewelry.objects.all().order_by('-jewelry_id')
        else:
            jewelry_list = Jewelry.objects.filter(status='pending').order_by('-jewelry_id')
    else:
        jewelry_list = Jewelry.objects.filter(owner=user).order_by('-jewelry_id')
    
    search_query = request.GET.get('search')
    if search_query:
        jewelry_list = jewelry_list.filter(name__icontains=search_query)
    
    # Sort
    sort_by = request.GET.get('sort')
    if sort_by:
        jewelry_list = jewelry_list.order_by(sort_by)
        
    # Pagination
    paginator = Paginator(jewelry_list, 5)  # Show 5 jewelry items per page
    page = request.GET.get('page')
    try:
        jewelries = paginator.page(page)
    except PageNotAnInteger:
        jewelries = paginator.page(1)
    except EmptyPage:
        jewelries = paginator.page(paginator.num_pages)
    
    return render(request, 'jewelry/my_jewelry_list.html', {'jewelries': jewelries})

@login_required
def jewelry_update_by_staff(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    
    if request.method == 'POST':
        preliminary_price = request.POST.get('preliminary_price')
        final_price = request.POST.get('final_price') if request.user.role == 'MANAGER' else jewelry.final_price
        received_at = request.POST.get('received_at')

        jewelry.preliminary_price = preliminary_price
        jewelry.final_price = final_price if request.user.role == 'MANAGER' else jewelry.final_price
        jewelry.received_at = received_at
        jewelry.save()

        return redirect('jewelry:jewelry-detail', pk=jewelry.pk)

    return render(request, 'jewelry/jewelry_update_by_staff.html', {'jewelry': jewelry})

@login_required
def jewelry_confirm_auction(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)

    if request.user != jewelry.owner:
        return HttpResponseForbidden("You are not the owner of this jewelry.")

    if request.method == 'POST':
        jewelry.seller_approved = True
        jewelry.save()
        return redirect('jewelry:jewelry-detail', pk=jewelry.pk)

    return render(request, 'jewelry/jewelry_confirm_auction.html', {'jewelry': jewelry})

@login_required
def jewelry_approve(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)

    if request.user.role not in ['STAFF', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to approve this jewelry.")

    if request.method == 'POST':
        jewelry.status = 'APPROVED'
        jewelry.save()
        return redirect('jewelry:jewelry-detail', pk=jewelry.pk)

    return render(request, 'jewelry/jewelry_approve.html', {'jewelry': jewelry})

@login_required
def jewelry_reject(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)

    if request.user.role not in ['STAFF', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to reject this jewelry.")

    if request.method == 'POST':
        jewelry.status = 'REJECTED'
        jewelry.save()