from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import Newsletter
from . import models


def get_newsletter(request):
    if request.method == 'POST':
        form = Newsletter(request.POST)

        if form.is_valid():
            new_form = models.Newsletter.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
            )

        return HttpResponseRedirect(reverse('newsletter:success'))
    
    else:
        form = Newsletter()

    context = {'form': form}
    return render(request, 'newsletter/form_page.html', context)


def success_newsletter(request):
    return render(request, 'contact/success.html')