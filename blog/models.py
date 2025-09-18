from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
 
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.png')
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    email = models.EmailField()
    message = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-datetime_created']

    def __str__(self):
        return self.author
