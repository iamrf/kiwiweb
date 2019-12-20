from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import Contact
from . import models



def get_contact(request):
    if request.method == "POST":
        form = Contact(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_form = models.Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                tel=form.cleaned_data['tel'],
                subject=form.cleaned_data['subject'],
                content=form.cleaned_data['content'],
                )
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contact:success'))
    else:
        form = Contact()

    context = {'form': form,}
    return render(request, 'contact/form_page.html', context)


def success_contact(request):
    return render(request, 'contact/success.html')