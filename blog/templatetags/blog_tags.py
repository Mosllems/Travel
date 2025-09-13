from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/blog-latest_blogs.html')
def get_latest_blogs(count=3):
    posts = Post.objects.filter(status=1)[:count]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-category.html')
def get_category():
    categories = Category.objects.all().order_by('name')
    return {'categories': categories}
