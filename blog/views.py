from django.shortcuts import render


def blogview(request):
    return render (request, "blog/blog-home.html")


def blogdetail(request):
    return render (request, "blog/blog-single.html")
