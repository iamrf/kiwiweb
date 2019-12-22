from django.shortcuts import render, get_object_or_404
from . import models
from offer.views import get_offer


def home(request):
    web_plans = models.website.published.order_by('sort')
    context = {'web_plans': web_plans,}
    return render(request, 'services/home.html', context)

def website(request, slug):
    plan = get_object_or_404(models.website, slug=slug)

    # Get offer from get_offer() function
    offer_price = get_offer(plan)

    context = {
        'plan': plan,
        'offer_price': offer_price,
    }
    return render(request, 'services/web_plan.html', context)