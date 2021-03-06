from django.shortcuts import render, get_object_or_404
from . import models


def home(request):
    posts = models.Post.published.order_by('-date')[:5]
    context = {'posts': posts,}
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    comments = post.comments.filter(publish=True).order_by('-created')
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post.html', context)


def categories(request):
    cats = models.Category.objects.all()
    context = {'cats': cats,}
    return render(request, 'blog/categories.html', context)


def category(request, slug):
    cat = get_object_or_404(models.Category, slug=slug)
    context = {'cat': cat,}
    return render(request, 'blog/category.html', context)


def tags(request):
    tags = models.Tag.objects.all()
    context = {'tags': tags,}
    return render(request, 'blog/tags.html', context)


def tag(request, slug):
    tag = get_object_or_404(models.Tag, slug=slug)
    context = {'tag': tag}
    return render(request, 'blog/tag.html', context)
