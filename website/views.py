from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been added successfully")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,

        })
