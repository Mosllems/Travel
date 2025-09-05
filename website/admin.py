from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'created_date']
    list_per_page = 10
    search_fields = ['name']

admin.site.register(Contact, ContactAdmin)
