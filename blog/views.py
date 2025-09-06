from django.shortcuts import render
from blog.models import Post


def blogview(request):
    posts = Post.objects.filter(status= 1)
    return render (request, "blog/blog-home.html", context= {
        'posts': posts,

        })


def blogdetail(request):
    return render (request, "blog/blog-single.html")
