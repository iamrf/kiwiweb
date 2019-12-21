from django.contrib import admin
from . import models

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'template', 'domain', 'host', 'price', 'created', 'publish', 'sort')
    list_filter = ('created', 'domain', 'template', 'price')
    search_fields = ('title', 'template', 'domain', 'host', 'support', 'created', 'desc', 'price')
    date_hierarchy = 'created'
    ordering = ['sort', 'title', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.website, WebsiteAdmin)