from django.shortcuts import render, get_object_or_404
from . import models


def home(request):
    posts = models.Post.published.order_by('-date')[:5]
    context = {'posts': posts,}
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    context = {'post': post,}
    return render(request, 'blog/detail.html', context)