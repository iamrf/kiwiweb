from django.db import models
from core.models import TimeStampedModel


class Contact(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    tel = models.CharField(max_length=15, blank=True, verbose_name="Tel")
    subject = models.CharField(max_length=250, verbose_name="Subject")
    content = models.TextField(verbose_name="Content")

    def __str__(self):
        return self.subject