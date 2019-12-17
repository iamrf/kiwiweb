from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields.
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    class Meta:
        abstract = True