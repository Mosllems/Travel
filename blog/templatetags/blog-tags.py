from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/templates/blog/blog-latest_blogs.html')
def get_latest_blogs(count=3):
    posts = Post.objects.filter('created_date')[:count]
    return {'posts': posts}
