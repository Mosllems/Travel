from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the homepage")


def about(request):
    return HttpResponse("About us")


def contact(request):
    return HttpResponse("Contact us")
