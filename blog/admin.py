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


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'modified', 'status')
    list_filter = ('created', 'modified', 'date', 'author')
    search_fields = ('title', 'content','author', 'date', 'created', 'modified', 'status',)
    date_hierarchy = 'date'
    ordering = ['-date', 'title', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)