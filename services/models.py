from django.db import models
from core.models import TimeStampedModel, PublishedManager
from django.urls import reverse


class website(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=200, verbose_name='Slug')
    template = models.CharField(max_length=200, verbose_name="Template")
    domain = models.CharField(max_length=200, verbose_name="Domain")
    host = models.CharField(max_length=200, verbose_name="Host")
    support = models.CharField(max_length=200, verbose_name="Support", blank=True)
    op_1 = models.CharField(max_length=200, verbose_name="Option 1", blank=True)
    op_2 = models.CharField(max_length=200, verbose_name="Option 2", blank=True)
    op_3 = models.CharField(max_length=200, verbose_name="Option 3", blank=True)
    op_4 = models.CharField(max_length=200, verbose_name="Option 4", blank=True)
    op_5 = models.CharField(max_length=200, verbose_name="Option 5", blank=True)
    op_6 = models.CharField(max_length=200, verbose_name="Option 6", blank=True)
    op_7 = models.CharField(max_length=200, verbose_name="Option 7", blank=True)
    op_8 = models.CharField(max_length=200, verbose_name="Option 8", blank=True)
    op_9 = models.CharField(max_length=200, verbose_name="Option 9", blank=True)
    desc = models.TextField(verbose_name="Description", blank=True)
    price = models.CharField(max_length=50, verbose_name="Price")
    sort = models.IntegerField(blank=True, null=True, verbose_name="Sorting")
    publish = models.BooleanField(verbose_name="Publish", default=True)

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # The published posts manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("services:website", kwargs={"slug": self.slug})
    