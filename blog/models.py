from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from core.models import TimeStampedModel, PublishedManager
from . import views


class Category(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('slug', '-created', '-modified')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"slug": self.slug})
    


class Tag(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title", unique=True)
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)

    class Meta:
        ordering = ('slug', '-created', '-modified')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:tag", kwargs={"slug": self.slug})


class Post(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name="Title")
    slug = models.SlugField(max_length=250, verbose_name="Slug", unique=True)
    content = models.TextField(verbose_name="Content")
    categories = models.ManyToManyField(Category, related_name="posts", blank=True, verbose_name="Categories")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True, verbose_name="Tags")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Author")
    date = models.DateTimeField(default=timezone.now, verbose_name="Publish date")
    publish = models.BooleanField(verbose_name="Publish", default=False)

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # The published posts manager

    class Meta:
        ordering: ('-date', 'title', 'author',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Post")
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    content = models.TextField(verbose_name="Content")
    publish = models.BooleanField(verbose_name="Publish", default=True)
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering: ('-created', 'name', 'email',)

    def __str__(self):
        return self.email
