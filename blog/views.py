from django.shortcuts import render
from . import models


def home(request):
    posts = models.Post.published.order_by('-date')[:5]
    context = {'posts': posts,}
    return render(request, 'blog/home.html', context)
