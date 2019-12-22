from django.contrib import admin
from . import models

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'type', 'start', 'end', 'created')
    list_filter = ('type', 'start', 'end', 'created')
    search_fields = ('title', 'amount', 'type', 'start', 'end')
    date_hierarchy = 'created'
    ordering = ('start', '-created', '-modified', 'title')


admin.site.register(models.Offer, OfferAdmin)