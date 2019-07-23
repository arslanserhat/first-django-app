# coding=utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def post_index(request):
    posts = post.objects.all()

    query = request.GET.get('q')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()


    paginator = Paginator(posts, 3)  # Show 25 contacts per page

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, slug):
    posts = get_object_or_404(post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.posts = posts
        comment.save()
        print(comment)
        return HttpResponseRedirect(posts.get_absolute_url())

    context = {
        'post': posts,
        'form': form
    }
    return render(request, "post/detail.html", context)

def post_create(request):
    if not request.user.is_authenticated:
        return Http404()


    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        posts_create = form.save(commit=False)
        posts_create.user = request.user
        posts_create.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(posts_create.get_absolute_url())
    context = {
        'form': form
    }

    return render(request, 'post/form.html', context)

def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    posts_update = get_object_or_404(post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=posts_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz.', extra_tags='mesaj-basarılı')
        return HttpResponseRedirect(posts_update.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    posts_delete = get_object_or_404(post, slug=slug)
    posts_delete.delete()
    return redirect('post:index')

