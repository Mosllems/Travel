from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'counted_view', 'created_date', 'modified_date', 'status']
    list_filter = ['status', 'author']
    list_per_page = 10
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post', 'status', 'email', 'datetime_created']
    list_filter = ['status', 'author']
    search_fields = ['author']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
