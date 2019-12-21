from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified',)
    list_filter = ('created', 'modified')
    search_fields = ('title', 'created', 'modified',)
    date_hierarchy = 'created'
    ordering = ['title', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified',)
    list_filter = ('created', 'modified')
    search_fields = ('title', 'created', 'modified',)
    date_hierarchy = 'created'
    ordering = ['title', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'modified', 'publish')
    list_filter = ('created', 'publish',)
    search_fields = ('title', 'desc','url', 'created', 'modified', 'publish',)
    date_hierarchy = 'created'
    ordering = ['slug', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)