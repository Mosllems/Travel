from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/blog-latest_blogs.html')
def get_latest_blogs(count=3):
    posts = Post.objects.filter(status=1)[:count]
    return {'posts': posts}
