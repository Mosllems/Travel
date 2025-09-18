from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post, Category
from taggit.models import Tag


def blogview(request):
    posts = Post.objects.filter(status=1).order_by("-created_date").prefetch_related('category')
    category = request.GET.get("category")
    tag = request.GET.get("tag")
    all_tags = Tag.objects.all()

    if category:
        posts = Post.objects.filter(status=1, category__name=category).order_by("-created_date").prefetch_related('category')
    if tag:
        posts = Post.objects.filter(status=1, tag__name=tag).order_by("-created_date").prefetch_related('category')

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render (request, "blog/blog-home.html", context= {
        'posts': posts,
        'tags': all_tags,
        
        })


def blogdetail(request, title):
    post = get_object_or_404(Post, title=title, status=1)
    return render (request, "blog/blog-single.html", context={
        'post': post,
    
    })


def search(request):
    if request.method=='GET':
        searched= request.GET.get('s')
        posts = Post.objects.filter(status=1,title__icontains=searched).order_by("-created_date")
    else:
        posts = Post.objects.filter(status=1).order_by("-created_date")
    return render (request, "blog/blog-home.html", context= {
        'posts': posts,
        
        })
