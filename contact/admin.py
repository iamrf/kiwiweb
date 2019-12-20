from django.contrib import admin
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'tel', 'created')
    list_filter = ('created', 'modified')
    search_fields = ('subject', 'content','name', 'email', 'tel')
    date_hierarchy = 'created'
    ordering = ('-created', 'subject', 'name')


admin.site.register(models.Contact, ContactAdmin)