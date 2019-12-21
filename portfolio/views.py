from django.shortcuts import render, get_object_or_404
from . import models


def home(request):
    portfolio = models.Portfolio.published.all()
    context = {'portfolio': portfolio,}
    return render(request, 'portfolio/home.html', context)


def item(request, slug):
    item = get_object_or_404(models.Portfolio, slug=slug)
    context = {'item': item,}
    return render(request, 'portfolio/item.html', context)