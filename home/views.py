from django.shortcuts import render
from services import models as services_models


def index(request):
    plans = services_models.website.published.all()
    context = {
        'plans': plans,
    }
    return render(request, 'home/index.html', context)
