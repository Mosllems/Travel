from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blogview(request):
    posts = Post.objects.filter(status= 1)
    return render (request, "blog/blog-home.html", context= {
        'posts': posts,

        })


def blogdetail(request, title):
    post = get_object_or_404(Post, title=title)
    return render (request, "blog/blog-single.html", context={
        'post': post,

    })
