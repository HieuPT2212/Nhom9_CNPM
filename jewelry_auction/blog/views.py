from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            if request.user.role in ['MANAGER', 'ADMIN']:
                blog.status = 'APPROVED'
                messages.success(request, 'Blog created successfully.')
            else:
                blog.status = 'PENDING'
                messages.success(request, 'Blog submitted for approval.')
            blog.save()
            return redirect('blog-list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form': form})

def blog_list(request):
    if request.user.is_authenticated and request.user.role in ['MANAGER', 'ADMIN']:
        blogs = Blog.objects.filter(status='APPROVED').order_by('-publication_date')
    else:
        blogs = Blog.objects.filter(status='APPROVED').order_by('-publication_date')

    search_query = request.GET.get('search')
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)

    # Sắp xếp
    sort_by = request.GET.get('ordering')
    if sort_by:
        blogs = blogs.order_by(sort_by)

    context = {'blogs': blogs}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)

@login_required
def blog_approve(request, pk):
    if request.user.role not in ['ADMIN', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to approve blogs.")

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.status = 'APPROVED'
        blog.save()
        messages.success(request, 'Blog approved successfully.')
        return redirect('blog-list')  # Hoặc chuyển hướng đến trang quản lý blog

    return render(request, 'blog/blog_approve.html', {'blog': blog})

@login_required
def blog_reject(request, pk):
    if request.user.role not in ['ADMIN', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to reject blogs.")

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.status = 'REJECTED'
        blog.save()
        messages.success(request, 'Blog rejected.')
        return redirect('blog-list')  # Hoặc chuyển hướng đến trang quản lý blog

    return render(request, 'blog/blog_reject.html', {'blog': blog})

@login_required
def blog_pending_list(request):
    if request.user.role not in ['ADMIN', 'MANAGER']:
        return HttpResponseForbidden("You don't have permission to view pending blogs.")

    blogs = Blog.objects.filter(status='PENDING').order_by('-publication_date')
    return render(request, 'blog/blog_pending_list.html', {'blogs': blogs})