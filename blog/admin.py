from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'counted_view', 'created_date', 'modified_date', 'status']
    list_filter = ['status']
    list_per_page = 10
    search_fields = ['title']

admin.site.register(Post, PostAdmin)