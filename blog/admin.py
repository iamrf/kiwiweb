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
    list_display = ('title', 'author', 'date', 'modified', 'publish')
    list_filter = ('date', 'author', 'publish',)
    search_fields = ('title', 'content','author', 'date', 'created', 'modified', 'publish',)
    date_hierarchy = 'date'
    ordering = ['-date', 'title', '-created', '-modified',]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'publish',)
    list_filter = ('created', 'publish',)
    search_fields = ('content','name', 'email', 'created', 'publish',)
    date_hierarchy = 'created'
    ordering = ['-created', 'name', 'email',]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)