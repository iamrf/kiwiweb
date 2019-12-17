from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('title', '-created', '-modified')

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('title', '-created', '-modified')

    def __str__(self):
        return self.title


# Define a manager for published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')


class Post(TimeStampedModel):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

    title = models.CharField(max_length=250, verbose_name="Title")
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)
    content = models.TextField(verbose_name="Content")
    categories = models.ManyToManyField(Category, blank=True, verbose_name="Categories")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tags")
    date = models.DateTimeField(default=timezone.now, verbose_name="Publish date")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # The published posts manager

    class Meta:
        ordering: ('-date', 'title', 'author',)

    def __str__(self):
        return self.title