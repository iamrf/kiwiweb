from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from .forms import Newsletter
from . import models


def get_newsletter(request):
    error_msg = False

    if request.method == 'POST':
        form = Newsletter(request.POST)

        if form.is_valid():
            try:
                new_form = models.Newsletter.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                )

            except IntegrityError:
                error_msg = 'این ایمیل قبلا در سیستم ثبت شده'

            else:
                return HttpResponseRedirect(reverse('newsletter:success'))

    else:
        form = Newsletter()

    context = {
        'form': form,
        'error': error_msg,
        }
    return render(request, 'newsletter/form_page.html', context)


def success_newsletter(request):
    return render(request, 'contact/success.html')