from django.db import models


# Define a abstract model contains created and modified datetime
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields.
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    class Meta:
        abstract = True


# Define a manager for published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publish=True)
