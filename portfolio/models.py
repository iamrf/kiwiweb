from django.db import models
from django.urls import reverse
from core.models import TimeStampedModel, PublishedManager


class Category(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('slug', '-created', '-modified')

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('slug', '-created', '-modified')

    def __str__(self):
        return self.title


class Portfolio(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title")
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)
    img = models.ImageField(upload_to="portfolio/templates/portfolio/img/", blank=True, verbose_name="Image")
    desc = models.TextField(verbose_name="Description")
    url = models.URLField(verbose_name="URL", blank=True)
    categories = models.ManyToManyField(Category, related_name="portfolios", blank=True, verbose_name="Categories")
    tags = models.ManyToManyField(Tag, related_name="portfolios", blank=True, verbose_name="Tags")
    publish = models.BooleanField(verbose_name="Publish", default=True)

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # The published posts manager

    class Meta:
        ordering: ('-date', 'title', 'author',)

    def __setr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:item", kwargs={"slug": self.slug})
    