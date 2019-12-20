from django.contrib import admin
from . import models


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('email', 'name', 'created')
    date_hierarchy = 'created'
    ordering = ('-created', 'email', 'name', '-modified')


admin.site.register(models.Newsletter, NewsletterAdmin)