from django.db import models
from core.models import TimeStampedModel


class Newsletter(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name="Name", blank=True)
    email = models.EmailField(verbose_name="Email", unique=True)

    def __str__(self):
        return self.email