from django.db import models
from core.models import TimeStampedModel


class Offer(TimeStampedModel):
    TYPE_CHOICES = (
        ('percent', '%'),
        ('absolute', '$'),
    )

    title = models.CharField(max_length=200, verbose_name="Title")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type")
    amount = models.IntegerField(verbose_name="Amount")
    start = models.DateTimeField(blank=True, null=True, verbose_name="Start date")
    end = models.DateTimeField(blank=True, null=True, verbose_name="End date")

    class Meta:
        ordering = ('start', '-modified',)

    def __str__(self):
        return self.title