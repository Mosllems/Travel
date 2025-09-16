from django.shortcuts import render
from django.http import HttpResponse

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
    form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,

        })
